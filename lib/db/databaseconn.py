import sqlite3

DATABASE_PATH = "meal-planner.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn
    

def create_tables():
    conn = get_db_connection()
    Cursor = conn.cursor()

    Cursor.execute("""
        CREATE TABLE IF NOT EXISTS mealcategories(
            id INTEGER PRIMARY KEY,
            name TEXT)
    """)

    Cursor.execute("""
        CREATE TABLE IF NOT EXISTS meals(
            id INTEGER PRIMARY KEY,
            name TEXT,
            mealcategories_id INTEGER,
            FOREIGN KEY(mealcategories_id) REFERENCES mealcategories(id))
    """)

    conn.commit()
    conn.close()

    

    
