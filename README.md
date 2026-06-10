#  SSL Certificate Expiry Watcher

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20Dashboard-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/SQLite-Database-07405E?style=for-the-badge&logo=sqlite">
  <img src="https://img.shields.io/badge/Ollama-Llama3-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Discord-Alerts-5865F2?style=for-the-badge&logo=discord">
  <img src="https://img.shields.io/badge/AI-Powered-red?style=for-the-badge">
</p>

<p align="center">
  <b>An intelligent AI-powered SSL observability platform for proactive certificate management</b>
</p>

---

##  Overview

SSL Certificate Expiry Watcher is a full-stack monitoring platform that tracks SSL certificates across multiple public domains, detects expiry risks, and generates AI-powered remediation tasks — all from a live web dashboard.

**Key capabilities:**
- Scans SSL certificates of public domains
- Detects and classifies expiry risks automatically
- Ranks domains by urgency
- Generates AI-powered renewal tasks via Ollama + Llama3
- Sends real-time Discord alerts
- Exports CSV and Markdown reports
- Displays a live auto-refreshing monitoring dashboard
- Stores full scan history in a SQLite database

---

##  Problem Statement

SSL certificates expire frequently and manual tracking leads to:

- Website downtime
- Browser security warnings
- Service interruptions
- Operational failures
- Loss of customer trust

Most monitoring tools only detect expiry — they do not suggest what to do next. This project solves both detection and remediation.

---

##  Solution

This platform combines several systems into one integrated tool:

| Layer | Component |
|---|---|
| Detection | SSL Scanner |
| Analysis | Risk Analysis Engine |
| Intelligence | AI Task Generator (Ollama + Llama3) |
| Prioritization | Ranking Engine |
| Notification | Real-Time Discord Alerts |
| Visualization | Flask Dashboard |
| Reporting | CSV + Markdown Report Generator |

---

##  Project Structure

```
ssl-expiry-watcher/
│
├── src/
│   ├── main.py              # Entry point — runs full scan pipeline
│   ├── scanner.py           # SSL certificate fetching and expiry calculation
│   ├── engine.py            # Risk analysis and status classification
│   ├── database.py          # SQLite insert and fetch operations
│   ├── app.py               # Flask web dashboard
│   ├── llm.py               # Ollama + Llama3 AI task generation
│   ├── ranker.py            # Domain urgency ranking logic
│   ├── report.py            # CSV and Markdown report generation
│   └── discord_alert.py     # Discord webhook alert integration
│
├── database/
│   └── ssl_data.db          # SQLite database (auto-created on first run)
│
├── data/
│   └── domains.csv          # Input list of domains to monitor
│
├── reports/
│   ├── ssl_report.csv       # Generated CSV report
│   └── ssl_report.md        # Generated Markdown report
│
├── src/templates/
│   └── dashboard.html       # Flask dashboard HTML template
│
└── README.md
```

---

##  Features

###  SSL Monitoring
- Fetches SSL certificate metadata for any public domain
- Calculates days remaining until expiry
- Detects invalid or unreachable certificates

###  Risk Analysis Engine

| Status | Meaning |
|---|---|
|  HEALTHY | Certificate is valid — no action needed |
|  WARNING | Expiring soon — renewal required |
|  BROKEN | Expired or invalid — urgent fix needed |
|  ERROR | Domain unreachable — investigate immediately |

###  AI Renewal Task Generator
Uses Ollama + Llama3 at runtime to generate:
- Unique SSL renewal tasks per domain
- Priority levels (HIGH / LOW)
- Owner placeholders for team assignment
- Specific step-by-step remediation actions

###  Discord Alert System
Automatically sends alerts for:
-  Certificates expiring soon (WARNING status)
-  Broken or expired certificates (BROKEN status)

###  Ranking System
- Domains with fewest days left are ranked first
- Critical incidents are prioritized at the top

###  Automated Reports
- CSV report — downloadable directly from the dashboard
- Markdown report — formatted and email-ready

###  Live Dashboard
- Real-time monitoring UI built with Flask
- Search and filter by domain name or status
- Status badges for at-a-glance visibility
- AI-generated task display per domain
- Auto-refreshes every 30 seconds

---

##  Tech Stack

| Technology | Usage |
|---|---|
| Python 3.12 | Backend |
| Flask | Web Dashboard |
| SQLite | Database |
| Pandas | CSV Processing |
| Ollama + Llama3 | AI Runtime (Task Generation) |
| Discord Webhooks | Alerts |
| ngrok | Public URL Tunneling |
| HTML / CSS | Frontend |

---

##  Input Format

Create a `data/domains.csv` file with one domain per row:

```csv
domain
google.com
github.com
wikipedia.org
openai.com
yourwebsite.com
```

---

##  How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ssl-expiry-watcher.git
cd ssl-expiry-watcher
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Ollama (AI Engine)
```bash
ollama pull llama3
ollama serve
```

### 5. Run the SSL Scanner
```bash
python src/main.py
```

### 6. Launch the Flask Dashboard
```bash
python src/app.py
```

### 7. Open in Browser
```
http://127.0.0.1:5000
```

### 8. Get a Public Shareable Link (Optional)
```bash
.\ngrok.exe http 5000
```

---

##  Outputs

| Output | Description |
|---|---|
|  SQLite Database | Full SSL monitoring history across all scans |
|  CSV Report | Ranked SSL domain report (downloadable) |
|  Markdown Report | Email-ready formatted report |
|  Discord Alerts | Real-time notifications for WARNING and BROKEN |
|  Dashboard | Live monitoring UI with filters and AI tasks |

---

##  System Architecture

```
domains.csv
    ↓
SSL Scanner
    ↓
Risk Analysis Engine
    ↓
Ollama AI Engine (Llama3)
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
##  Screenshots

> Dashboard — Main monitoring view with status badges and AI tasks
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/838318cd-ecae-4d95-9636-9eb5f507bac0" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fb5ee3a4-d787-458b-a4f6-9d9f076c88ea" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/dbe1a193-9577-438b-92cc-94178024b555" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2695ba3b-d6db-4694-ba32-c6cc3994b602" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9dfffdcf-65e6-4dee-ae21-bdd5ed6f1f1f" />



