import sqlite3

DATABASE_PATH = "meal-planner.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)