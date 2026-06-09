# SSL Certificate Expiry Watcher

<p align="center">

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/Flask-Web%20Dashboard-black?style=for-the-badge&logo=flask">

<img src="https://img.shields.io/badge/SQLite-Database-07405E?style=for-the-badge&logo=sqlite">

<img src="https://img.shields.io/badge/Ollama-Llama3-green?style=for-the-badge">

<img src="https://img.shields.io/badge/Discord-Alerts-5865F2?style=for-the-badge&logo=discord">

<img src="https://img.shields.io/badge/AI-Powered-red?style=for-the-badge">

<img src="https://img.shields.io/badge/Hackathon-Project-orange?style=for-the-badge">

</p>

---

#  Overview

An intelligent  SSL monitoring platform that:

✅ Scans SSL certificates of public domains
✅ Detects expiry risks
✅ Ranks domains by urgency
✅ Generates AI-powered renewal tasks
✅ Sends Discord alerts
✅ Exports CSV & Markdown reports
✅ Displays live monitoring dashboard

---

#  Problem Statement

SSL certificates expire frequently and manual tracking can cause:

* 🔴 Website downtime
* 🔴 Browser security warnings
* 🔴 Service interruptions
* 🔴 Operational failures
* 🔴 Loss of customer trust

Most monitoring systems only detect expiry but do not suggest remediation steps.

---

#  Solution

This project combines:

*  SSL Monitoring
*  Risk Analysis
*  AI Task Generation
*  Ranking Engine
*  Real-Time Alerts
*  Dashboard Visualization
*  Automated Reporting

to build a complete AI-powered SSL observability platform.

---

#  AI Usage

| AI Tool         | Purpose                                      |
| --------------- | -------------------------------------------- |
| ChatGPT         | Backend development, debugging, architecture |
| Gemini AI       | Frontend dashboard UI improvements           |
| Ollama + Llama3 | Runtime AI renewal task generation           |

---

#  System Architecture

```text id="zr8fd8"
 domains.csv
        ↓
 SSL Scanner
        ↓
 Risk Engine
        ↓
 Ollama AI Engine
        ↓
 SQLite Database
        ↓
 Discord Alerts
        ↓
 Ranking System
        ↓
 CSV + Markdown Reports
        ↓
 Flask Dashboard
```

---

# 📁 Project Structure

```text id="6i5bfg"
📦 ssl-expiry-watcher
│
├── 📂 src/
│   ├── main.py
│   ├── scanner.py
│   ├── engine.py
│   ├── database.py
│   ├── dashboard.py
│   ├── llm.py
│   ├── ranker.py
│   ├── report.py
│   └── discord_alert.py
│
├── 📂 database/
│   └── ssl_data.db
│
├── 📂 data/
│   └── domains.csv
│
├── 📂 output/
│   ├── report.csv
│   └── report.md
│
├── 📂 templates/
│   └── dashboard.html
│
└── README.md
```

---

#  Features

##  SSL Monitoring

* Fetch SSL certificate metadata
* Calculate expiry days
* Detect invalid certificates

---

##  Risk Analysis Engine

Classifies domains into:

* 🟢 HEALTHY
* 🟡 WARNING
* 🔴 BROKEN

---

##  AI Renewal Task Generator

Uses Ollama + Llama3 to generate:

* SSL renewal tasks
* Priority levels
* Owner placeholders
* Suggested remediation steps

---

##  Discord Alert System

Automatically sends alerts for:

* Expiring certificates
* Broken SSL certificates

---

##  Ranking System

Ranks domains by urgency:

* Lowest days left first
* Critical incidents prioritized

---

##  Automated Reports

Generates:

*  CSV reports
*  Email-ready Markdown reports

---

##  Dashboard

Provides:

* Live monitoring UI
* Search & filtering
* Status badges
* AI-generated task display
* Auto-refreshing dashboard

---

#  Input Example

## domains.csv

```csv id="m2edk0"
domain
google.com
github.com
wikipedia.org
openai.com
```

---

#  AI Output Example

```json id="1xjlwm"
{
  "task": "Renew SSL certificate for wikipedia.org",
  "priority": "P1",
  "owner": "platform-team",
  "action": "Generate new certificate and update DNS configuration"
}
```

---

#  How to Run

## 1️⃣ Clone Repository

```bash id="p5snr5"
git clone https://github.com/your-username/ssl-expiry-watcher.git
```

---

## 2️⃣ Open Project Folder

```bash id="ojphrg"
cd ssl-expiry-watcher
```

---

## 3️⃣ Create Virtual Environment

```bash id="qfr0h6"
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash id="k22gdl"
venv\Scripts\activate
```

---

## 5️⃣ Install Dependencies

```bash id="t38lva"
pip install -r requirements.txt
```

---

## 6️⃣ Start Ollama

```bash id="s8y0j7"
ollama run llama3
```

Keep this terminal running.

---

## 7️⃣ Run Main Monitoring System

```bash id="z5z4c0"
python src/main.py
```

---

## 8️⃣ Run Flask Dashboard

```bash id="f2a5hg"
python src/dashboard.py
```

---

## 9️⃣ Open Browser

```text id="fscs1k"
http://127.0.0.1:5000
```

---

#  Outputs Generated

| Output             | Description             |
| ------------------ | ----------------------- |
|  SQLite DB       | SSL monitoring history  |
|  CSV Report      | Ranked SSL report       |
|  Markdown Report | Email-ready report      |
|  Discord Alert   | Real-time notifications |
|  Dashboard       | Live monitoring UI      |

---

#  Tech Stack

| Technology       | Usage          |
| ---------------- | -------------- |
| Python           | Backend        |
| Flask            | Dashboard      |
| SQLite           | Database       |
| Pandas           | CSV Processing |
| Ollama           | AI Runtime     |
| Llama3           | AI Model       |
| Discord Webhooks | Alerts         |
| HTML/CSS         | Frontend       |

---

# 🔄 Workflow

```text id="ryu9tr"
Input Domains
      ↓
SSL Certificate Scan
      ↓
Risk Classification
      ↓
AI Renewal Task Generation
      ↓
Database Storage
      ↓ 
Discord Notifications
      ↓
Ranking Engine
      ↓
CSV + Markdown Export
      ↓
Dashboard Visualization
```

---
# Screenshots
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/838318cd-ecae-4d95-9636-9eb5f507bac0" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fb5ee3a4-d787-458b-a4f6-9d9f076c88ea" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/dbe1a193-9577-438b-92cc-94178024b555" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2695ba3b-d6db-4694-ba32-c6cc3994b602" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9dfffdcf-65e6-4dee-ae21-bdd5ed6f1f1f" />





