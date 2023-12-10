import sqlite3
from src.features.debug.debug import LOGGER


class SqliteCtrl_1:
    def __init__(self, dbPath) -> None:
        self.dbPath = dbPath

    def dict_factory(self, cursor: sqlite3.Cursor, row) -> dict:
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def db_connect(self, dbPath) -> sqlite3.Connection:
        conn: sqlite3.Connection = sqlite3.connect(dbPath)
        conn.row_factory = self.dict_factory
        return conn

    def read_db(self, query, params=None, is_one=False):
        try:
            conn: sqlite3.Connection = self.db_connect()
            cur: sqlite3.Cursor = conn.cursor()
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            if is_one:
                return cur.fetchone()
            return cur.fetchall()
        except sqlite3.Error as e:
            LOGGER().error(f"[SQLITE READ ERROR] {e.args[0]}")
            return False

    def write_into_db(self, query, params=None, lastRowId=False):
        try:
            conn: sqlite3.Connection = self.db_connect()
            cur: sqlite3.Cursor = conn.cursor()
            if cur.execute(query, params):
                conn.commit()
                if lastRowId:
                    return cur.lastrowid
                return True
            return False
        except sqlite3.Error as e:
            LOGGER().error(f"[SQLITE WRITE ERROR] {e.args[0]}")
            return False
