import sqlite3

CONN = sqlite3.connect('lib/db/mealplanner.db')
CURSOR = CONN.cursor()

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS mealcategories(
        id INTEGER PRIMARY KEY,
        name TEXT)
""")



