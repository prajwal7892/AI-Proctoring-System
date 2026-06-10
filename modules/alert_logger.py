import sqlite3
from datetime import datetime


class AlertLogger:

    def __init__(self):

        self.conn = sqlite3.connect(
            "alerts.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            alert_type TEXT,
            image_path TEXT
        )
        """)

        self.conn.commit()

    def log_alert(self, alert_type, image_path):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.cursor.execute("""
        INSERT INTO alerts(
            timestamp,
            alert_type,
            image_path
        )
        VALUES (?, ?, ?)
        """,
        (
            timestamp,
            alert_type,
            image_path
        ))

        self.conn.commit()

        print(
            f"[DB LOGGED] {timestamp} | {alert_type}"
        )