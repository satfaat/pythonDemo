from src.dbDemo.ex_sqlite.db_config import CONN, CURSOR


class Song:
    def __init__(self, name, album) -> None:
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls, req) -> None:
        with CONN:
            CURSOR.execute(req)
            CONN.commit()

    @classmethod
    def insert_data(cls, req, data) -> None:
        with CONN:
            CURSOR.execute(req, data)
            CONN.commit()

    @classmethod
    def show_table(cls, req) -> None:
        CURSOR.execute(req)
        rows = CURSOR.fetchall()
        return rows
