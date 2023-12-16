

class TinydbCtrl:
    def __init__(self, dbpath, tb_name: str) -> None:
        self.db_table = dbpath.table(tb_name)

    def insert_data_into_tb(self, data) -> None:
        self.db_table.insert(data)

    def all(self) -> None:
        self.db_table.all()
