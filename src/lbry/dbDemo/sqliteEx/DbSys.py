from src.dbDemo.ex_sqlite.db_config import CONN, CURSOR


class DbSys:

    @classmethod
    def sqlite_ver(cls) -> None:
        with CONN:
            CONN.execute("select sqlite_version()").fetchall()
