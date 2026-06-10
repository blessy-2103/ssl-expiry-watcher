import json
import os
import re
import pandas as pd

from database import init_db, insert_record
from discord_alert import send_alert
from engine import incident_engine, renewal_engine, service_status
from llm import generate_task
from ranker import rank_domains
from report import export_csv, export_markdown
from scanner import get_ssl_expiry


def safe_parse_llm(raw):
    """Safely parse Ollama response with robust fallback extractors for lists or strings."""
    if not raw:
        return None

    cleaned_raw = raw.strip().strip("```json").strip("```").strip()

    # Try standard load first
    try:
        return json.loads(cleaned_raw)
    except json.JSONDecodeError:
        pass

    # Regex Extractor: Rescues data from minor trailing commas or malformed formatting stutters
    try:
        extracted = {}
        for key in ["task", "priority", "owner"]:
            match = re.search(f'"{key}"\\s*:\\s*"([^"]+)"', cleaned_raw, re.DOTALL)
            if match:
                extracted[key] = match.group(1)
        
        # Pull actions safely if returned as an array string block
        action_block_match = re.search(r'"action"\s*:\s*\[(.*?)\]', cleaned_raw, re.DOTALL)
        if action_block_match:
            actions = re.findall(r'"([^"]+)"', action_block_match.group(1))
            if actions:
                extracted["action"] = actions
        else:
            action_text_match = re.search(r'"action"\s*:\s*"(.*?)"', cleaned_raw, re.DOTALL)
            if action_text_match:
                extracted["action"] = action_text_match.group(1)

        if "task" in extracted:
            return extracted
    except:
        return None
    return None


def main():
    init_db()

    os.makedirs("data", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    csv_input_path = "data/domains.csv"
    if not os.path.exists(csv_input_path):
        print(f"❌ Input file not found at {csv_input_path}.")
        return

    df = pd.read_csv(csv_input_path)
    results = []

    for domain in df["domain"]:
        domain = domain.strip()
        try:
            ssl = get_ssl_expiry(domain)
            days_left = ssl["days_left"]
            expiry_date = ssl.get("expiry_date", "—")

            status = service_status(days_left)
            incident = incident_engine(days_left)
            renewal = renewal_engine(days_left)

            # Query AI Insights
            raw_task = generate_task(domain, days_left, status)
            task_obj = safe_parse_llm(raw_task)

            # Establish strict default fallbacks if communication cuts out completely
            priority = "HIGH" if status in ["BROKEN", "ERROR", "WARNING"] else "LOW"
            owner = "secops-triage-team" if status == "WARNING" else "oncall-core-engineer" if status in ["BROKEN", "ERROR"] else "platform-team"
            task_title = f"Review SSL Certificate configuration for {domain}"
            action_steps = "• Run standard diagnostics scan.\n• Verify infrastructure path availability."

            if task_obj:
                task_title = task_obj.get("task", task_title).strip()
                priority = task_obj.get("priority", priority).strip().upper()
                if priority not in ["HIGH", "LOW"]:
                    priority = "HIGH" if status in ["BROKEN", "ERROR", "WARNING"] else "LOW"

                llm_owner = task_obj.get("owner", owner).strip().lower()
                if llm_owner not in ["unassigned", "none", "", "null"]:
                    owner = llm_owner

                raw_actions = task_obj.get("action", [])
                formatted_steps = []

                # --- MULTI-TYPE STRUCTURAL RECOVERY UNPACKER ---
                if isinstance(raw_actions, list):
                    for item in raw_actions:
                        if isinstance(item, dict):
                            # Unpack potential dictionary stutters like {'step 1': 'action description'}
                            for val in item.values():
                                if val:
                                    formatted_steps.append(str(val).strip())
                        else:
                            if item:
                                formatted_steps.append(str(item).strip())

                elif isinstance(raw_actions, dict):
                    # Unpack raw direct root object dictionary values
                    for val in raw_actions.values():
                        if val:
                            formatted_steps.append(str(val).strip())

                else:
                    # Cleanly split text blocks and string sequences containing literal string arrays
                    lines = [line.strip() for line in re.split(r'\\n|\n', str(raw_actions)) if line.strip()]
                    for line in lines:
                        formatted_steps.append(line)

                # Process all items cleanly to strip out duplicate markdown bullet elements or numbers
                final_clean_steps = []
                for step in formatted_steps:
                    clean_text = re.sub(r"^[•\-\*\s\d\.\:]+", "", step).strip()
                    if clean_text:
                        final_clean_steps.append(f"• {clean_text}")

                action_steps = "\n".join(final_clean_steps) if final_clean_steps else f"• Run routine infrastructure check for {domain}."

            # Build standard markdown report matching UI framework design requirements
            formatted_task_report = (
                f"📋 **Task:** {task_title}\n\n"
                f"🚨 **Priority:** {priority}\n\n"
                f"⚙️ **Action Steps:**\n{action_steps}"
            )

            # Save operation logs to database row records
            insert_record(domain, expiry_date, days_left, status, incident, renewal, formatted_task_report, owner)

            if status in ["WARNING", "BROKEN"]:
                try:
                    send_alert(domain, days_left, status)
                except Exception as e:
                    print(f"Discord error for {domain}: {e}")

            results.append({
                "domain": domain, "expiry_date": expiry_date, "days_left": days_left,
                "status": status, "incident": incident, "renewal": renewal,
                "task": formatted_task_report, "owner": owner, "priority": priority, "action": action_steps
            })

            print(f"📊 Processed: {domain} -> Status: {status} ({priority}) -> Assigned: {owner}")

        except Exception as e:
            print(f"❌ SSL scan failed for {domain}: {e}")
            results.append({
                "domain": domain, "expiry_date": "—", "days_left": -1, "status": "ERROR",
                "incident": "BROKEN", "renewal": "NO_ACTION", "task": f"SCAN FAILED: {str(e)}",
                "owner": "oncall-core-engineer", "priority": "HIGH", "action": "N/A"
            })

    ranked = rank_domains(results)
    export_csv(ranked, filename="reports/ssl_report.csv")
    export_markdown(ranked, filename="reports/ssl_report.md")
    print("\n✔ PIPELINE REFRESH COMPLETE")


if __name__ == "__main__":
    main()