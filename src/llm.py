import requests
import json

def generate_task(domain, days_left, status):
    """Queries local Ollama instance to generate a structured security ticket with an owner."""
    
    url = "http://localhost:11434/api/generate"
    
    prompt = f"""
    You are a Senior Infrastructure Security Engineer triage assistant. 
    Analyze this asset state:
    - Domain: {domain}
    - Days Left: {days_left}
    - Status: {status}

    Generate a custom remediation task. You must return your response as a strict, valid JSON object following this exact template structure:
    {{
        "task": "A unique, custom task title specifically mentioning the domain {domain}",
        "priority": "HIGH or LOW (Strict Rule: HIGH if status is BROKEN, ERROR, or WARNING. LOW if status is HEALTHY)",
        "owner": "oncall-core-engineer or secops-triage-team or platform-team",
        "action": [
            "Specific custom step 1 tailored for handling {domain}",
            "Specific custom step 2 tailored for handling {domain}"
        ]
    }}

    Return ONLY the raw JSON string. Do not wrap it in markdown code blocks or include any conversational intro text.
    """

    data = {
        "model": "llama3",  
        "prompt": prompt,
        "stream": False,
        "format": "json"    # Enforces strict JSON validation in Ollama
    }

    try:
        response = requests.post(url, json=data, timeout=30)
        if response.status_code == 200:
            return response.json().get("response", "")
    except Exception as e:
        print(f"LLM Connection Error: {e}")
    
    return ""