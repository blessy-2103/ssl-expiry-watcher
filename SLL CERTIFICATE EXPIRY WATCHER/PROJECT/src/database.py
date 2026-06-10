import sqlite3

DB_PATH = "database/ssl_data.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS ssl_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domain TEXT,
        expiry_date TEXT,
        days_left INTEGER,
        status TEXT,
        incident TEXT,
        renewal TEXT,
        task TEXT,
        owner TEXT,
        checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def insert_record(domain, expiry_date, days_left, status, incident, renewal, task, owner):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO ssl_history
        (domain, expiry_date, days_left, status, incident, renewal, task, owner)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        domain,
        expiry_date,
        days_left,
        status,
        incident,
        renewal,
        task,
        owner
    ))

    conn.commit()
    conn.close()