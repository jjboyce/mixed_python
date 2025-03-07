### CREATE AUDIT TABLE ###

import sqlite3
from datetime import date
conn = sqlite3.connect("/Users/johnboyce/vs_code_projects/budget_manager/budget.db")
cursor = conn.cursor()

today = date.today()


def create_audit_table():
    create_table_query = f"""
    CREATE TABLE audit (
    tr_id INTEGER PRIMARY KEY,
    date DATE,
    comment TEXT
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
    print(f"Audit Table Created")

create_audit_table()