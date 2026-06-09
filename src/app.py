import os
import sqlite3
from flask import Flask, render_template, request, send_from_directory

# Import the export handlers from your report.py file
from report import export_csv, export_markdown

app = Flask(__name__)

DB_PATH = "database/ssl_data.db"
REPORTS_DIR = os.path.join(os.getcwd(), "reports")


def fetch_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Optimized Query: Uses a subquery window function (ROW_NUMBER) to isolate the 
    # absolute latest record per unique domain based on the 'checked_at' timestamp.
    cur.execute("""
        WITH RankedLogs AS (
            SELECT domain, expiry_date, days_left, status,
                   incident, renewal, checked_at, task, owner,
                   ROW_NUMBER() OVER (PARTITION BY domain ORDER BY checked_at DESC) as rn
            FROM ssl_history
        )
        SELECT domain, expiry_date, days_left, status,
               incident, renewal, checked_at, task, owner
        FROM RankedLogs
        WHERE rn = 1
        ORDER BY days_left ASC
    """)

    rows = cur.fetchall()
    conn.close()

    # SAFE NORMALIZATION
    cleaned = []
    for r in rows:
        cleaned.append((
            r[0],                 # domain
            r[1] or "—",          # Cleaned: Using a clean dash instead of text "N/A"
            r[2],                 # days_left
            r[3] or "ERROR",      # status
            r[4] or "—",          # incident
            r[5] or "—",          # renewal
            r[6],                 # checked_at
            r[7] or "No AI task", # task
            r[8] or "unassigned"  # owner
        ))

    return cleaned


def get_summary(rows):
    # Initializes counters
    summary = {
        "HEALTHY": 0,
        "WARNING": 0,
        "BROKEN": 0,
        "ERROR": 0,
        "TOTAL": len(rows)
    }

    for r in rows:
        status = r[3]
        if status in summary:
            summary[status] += 1
        else:
            summary["ERROR"] += 1  # Catches unexpected status anomalies safely

    return summary


def get_filtered_data(search, filter_status):
    """Helper logic to get structured, filtered data for both views and exports."""
    data = fetch_data()

    # SEARCH FILTER
    if search:
        data = [d for d in data if search in d[0].lower()]

    # STATUS FILTER
    if filter_status != "ALL":
        data = [d for d in data if d[3] == filter_status]
        
    return data


@app.route("/")
def dashboard():
    search = request.args.get("search", "").strip().lower()
    filter_status = request.args.get("status", "ALL")

    # Fetch data filtered by the user's current search/status view criteria
    data = get_filtered_data(search, filter_status)

    # Dynamically tracks summary indicators against current viewport datasets
    summary = get_summary(data)

    return render_template(
        "dashboard.html",
        data=data,
        summary=summary,
        search=search,
        filter_status=filter_status
    )


@app.route('/download/csv')
def download_csv():
    """Converts viewport dataset to a structured spreadsheet download."""
    search = request.args.get("search", "").strip().lower()
    filter_status = request.args.get("status", "ALL")
    
    raw_data = get_filtered_data(search, filter_status)
    
    # Map the list of tuples to dictionaries so report.py's DictWriter can parse it
    formatted_list = []
    for r in raw_data:
        formatted_list.append({
            "domain": r[0],
            "expiry_date": r[1],
            "days_left": r[2],
            "status": r[3],
            "incident": r[4],
            "renewal": r[5],
            "checked_at": r[6],
            "task": r[7],
            "owner": r[8]
        })
        
    # Generate the file inside the reports folder
    csv_filename = os.path.join(REPORTS_DIR, "ssl_report.csv")
    export_csv(formatted_list, filename=csv_filename)
    
    try:
        return send_from_directory(
            directory=REPORTS_DIR,
            path="ssl_report.csv",
            as_attachment=True,
            download_name="ssl_report.csv"
        )
    except FileNotFoundError:
        return "⚠️ Error generating CSV File.", 404


@app.route('/download/markdown')
def download_markdown():
    """Converts viewport dataset to a clean Markdown template file download."""
    search = request.args.get("search", "").strip().lower()
    filter_status = request.args.get("status", "ALL")
    
    raw_data = get_filtered_data(search, filter_status)
    
    # Map the list of tuples to dictionaries so report.py can parse it
    formatted_list = []
    for r in raw_data:
        formatted_list.append({
            "domain": r[0],
            "expiry_date": r[1],
            "days_left": r[2],
            "status": r[3],
            "incident": r[4],
            "renewal": r[5],
            "checked_at": r[6],
            "task": r[7],
            "owner": r[8]
        })
        
    # Generate the file inside the reports folder
    md_filename = os.path.join(REPORTS_DIR, "ssl_report.md")
    export_markdown(formatted_list, filename=md_filename)
    
    try:
        return send_from_directory(
            directory=REPORTS_DIR,
            path="ssl_report.md",
            as_attachment=True,
            download_name="ssl_report.md"
        )
    except FileNotFoundError:
        return "⚠️ Error generating Markdown File.", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)