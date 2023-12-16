
from tinydb import TinyDB
from configs.dbConf.dbParams import dto_db


def tinydb(path_db) -> TinyDB:
    tinydb: TinyDB = TinyDB(path_db)
    return tinydb


dto_tdb: TinyDB = tinydb(dto_db)
