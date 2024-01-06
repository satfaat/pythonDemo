
import configs.dbConf.dbParams as dbParams
from tinydb import TinyDB


def tinydb(path_db) -> TinyDB:
    """Connect to databse via tinyDB"""
    tinydb: TinyDB = TinyDB(path_db)
    return tinydb


# db connection
dtoDB_conn: TinyDB = tinydb(dbParams.dtoDB_path)
# db tables
...

# db connection
siteDB_conn: TinyDB = tinydb(dbParams.siteDB_path)
# db tables
tb_menu_1 = siteDB_conn.table('menu1')

# db connection
dataDB_conn: TinyDB = tinydb(dbParams.dataDB_path)
# db tables
tb_users = siteDB_conn.table('Users')
