import csv
import os

def export_csv(data, filename="reports/ssl_report.csv"):
    # Ensure the reports directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    if not data:
        return
        
    keys = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def export_markdown(data, filename="reports/ssl_report.md"):
    # Ensure the reports directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    if not data:
        return

    md = "# 🔐 SSL/TLS Infrastructure Status Report\n\n"
    md += "An automated security scan of public endpoint certificates has identified infrastructure assets requiring immediate engineering intervention.\n\n"

    for d in data:
        md += f"""## Domain: {d['domain']}
- **Time Remaining to Expiry:** {d['days_left']} Days
- **Current Operational Status:** `{d['status']}`
- **Assigned Engineering Owner:** `{d['owner']}`
- **Remediation Action Blueprint Plan:**

{d['task']}

---
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(md)