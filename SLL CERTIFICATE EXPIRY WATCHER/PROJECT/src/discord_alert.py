import requests

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1513795375410970734/NWp_p3c9uCRm3an64Mj0658Bv_eO1byN00fAZg5xspFjh2pf-FxQuIFJEeU73h17QcDd"


def send_alert(domain, days_left, status):

    # 🎯 Choose emoji based on severity
    if status == "WARNING":
        emoji = "🚨"
        action = "Monitor certificate and plan renewal"
    elif status == "BROKEN":
        emoji = "🚨"
        action = "URGENT: Certificate is invalid or expired"
    else:
        emoji = "ℹ️"
        action = "No action required"

    message = f"""
{emoji} SSL ALERT 🚨

Domain: {domain}
Status: {status}
Days Left: {days_left}

Action Required: {action}
"""

    response = requests.post(WEBHOOK_URL, json={"content": message})

    if response.status_code == 204:
        print("Discord alert sent ✔")
    else:
        print("Discord alert failed ❌", response.text)