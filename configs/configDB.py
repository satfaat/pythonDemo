from sqlmodel import create_engine
from configs.dbConf.dbParams import sqlite_url


# connect_args only for sqlite
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
