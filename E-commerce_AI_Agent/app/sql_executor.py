import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def run_sql(sql: str):
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT", 5432)
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    
    # Extract column names from cursor
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    
    # Convert rows to list of dicts (with column names as keys)
    results = [dict(zip(column_names, row)) for row in rows]

    cursor.close()
    conn.close()
    return results

