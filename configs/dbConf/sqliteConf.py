from src.features.db.sqlite.SqliteCur_1 import SqliteCur_1
from configs.dbConf.dbParams import sqlite_db_path


sqlite: SqliteCur_1 = SqliteCur_1(sqlite_db_path)
