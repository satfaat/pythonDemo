import sqlite3


class DataBase:
    def __init__(self, DBNAME, TBNAME) -> None:
        self.TABLE_NAME = TBNAME
        self.DB_NAME = DBNAME
        self.CONN = sqlite3.connect(self.DB_NAME)
        self.CURSOR = self.CONN.cursor()

    def create_table(self, sql) -> None:
        with self.CONN:
            self.CURSOR.execute(sql)

    def insert_into(self, data) -> None:
        with self.CONN:
            self.CURSOR.execute(
                f'''INSERT INTO {self.TABLE_NAME} VALUES(?,?,?)''', data
            )

    def save_data(self) -> None:
        self.CONN.commit()

    def close_db(self) -> None:
        self.CONN.close()

    def select_all_from_table(self):
        self.CURSOR.execute(
            f'select * FROM {self.TABLE_NAME}')
        records = self.CURSOR.fetchall()
        return records

    def select_by_name(self, name):
        self.CURSOR.execute(
            f'SELECT * FROM {self.TABLE_NAME} WHERE name=?', (name,)
        )
        record = self.CURSOR.fetchone()
        return record

    def select_by_id(self, id):
        self.CURSOR.execute(
            f'SELECT * FROM {self.TABLE_NAME} WHERE id=?', (id,)
        )
        record = self.CURSOR.fetchone()
        return record

    def delete_by_id(self, id):
        self.CURSOR.execute(
            f'DELETE FROM {self.TABLE_NAME} WHERE id=?',
            (id,)
        )

    def drop_table(self):
        self.CURSOR.execute(
            f'DROP TABLE IF EXISTS {self.TABLE_NAME}'
        )
