import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_alert(domain, days_left):

    prompt = f"""
You are an IT Operations Engineer.

Write a professional SSL certificate expiry alert.

Domain: {domain}
Days left: {days_left}

Format:
- Severity
- Impact
- Recommendation
- Short ticket message
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


# TEST
if __name__ == "__main__":
    print(generate_alert("google.com", 10))