import schedule
import time
import os


def run_scan():
    print("🔄 Running SSL scan...")
    os.system("python src/main.py")


# Run every 6 hours
schedule.every(6).hours.do(run_scan)

print("⏰ Scheduler started (every 6 hours)")

while True:
    schedule.run_pending()
    time.sleep(60)