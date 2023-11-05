from src.dbDemo.ex_sqlite.Song import Song
from src.dbDemo.ex_sqlite.db_config import CONN


songs_tb = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
insert_song = """INSERT INTO songs VALUES (1, ?, ?)"""
data = ('Best', 'Mozartello')

req_get_all = """SELECT * FROM songs"""

Song('Best', 'Mozartello').create_table(songs_tb)
Song('Best', 'Mozartello').insert_data(insert_song, data)
rows = Song('Best', 'Mozartello').show_table(req_get_all)
print(rows)
CONN.close()
