from tinydb import TinyDB
from src.features.dbDemo.sqliteEx.SqliteCtrl_1 import SqliteCtrl_1
from sqlmodel import create_engine


dto_db = '../.dbs/dto.json'
sqlite_db_path = '../.dbs/oth.sqlite'
sqlite_url = f"sqlite:///{sqlite_db_path}"


def tinydb(path_db) -> TinyDB:
    tinydb: TinyDB = TinyDB(path_db)
    return tinydb


dto_tdb: TinyDB = tinydb(dto_db)


sqlite: SqliteCtrl_1 = SqliteCtrl_1(sqlite_db_path)

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
