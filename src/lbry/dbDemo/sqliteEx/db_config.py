import sqlite3

CONN = sqlite3.connect('.tmp\music.db')  # ":memory:"
CURSOR = CONN.cursor()
