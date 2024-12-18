import sqlite3

CONN = sqlite3.connect('lib/db/mealplanner.db')
CURSOR = CONN.cursor()