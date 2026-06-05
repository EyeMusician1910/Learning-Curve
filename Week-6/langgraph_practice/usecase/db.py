from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).with_name("claims.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    schema_sql = """
    CREATE TABLE IF NOT EXISTS claims (
        claim_id TEXT PRIMARY KEY,
        patient_id INTEGER NOT NULL,
        status TEXT NOT NULL,
        decision_details TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """

    with get_connection() as conn:
        conn.execute(schema_sql)
        conn.commit()

