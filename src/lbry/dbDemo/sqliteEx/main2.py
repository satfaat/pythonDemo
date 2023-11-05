from src.dbDemo.ex_sqlite.DataBase import DataBase
from src.dbDemo.ex_sqlite.dto.DbDto import DbDto
from src.dbDemo.ex_sqlite.dto.SongDto import SongDto


db_params = DbDto('.tmp/music2.db', 'songs')
rec1 = SongDto(2, 'Web', 'Mozartello')
data = (rec1.id, rec1.name, rec1.album)

db = DataBase(db_params.name, db_params.table)

sql_create = f'''CREATE TABLE IF NOT EXISTS {db_params.table}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, 
            album TEXT
        )'''
# db.create_table(sql_create)
# db.insert_into(data)
tb_data = db.select_all_from_table()
# storm = db.select_by_name('Stormy')
print(tb_data)
# print(storm)
db.delete_by_id(1)
db.save_data()
db.close_db()
# db.drop_table()
