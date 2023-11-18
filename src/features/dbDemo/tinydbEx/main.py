from tinydb import TinyDB, Query, where
from src.features.dbDemo.tinydbEx.TinydbCtrl import TinydbCtrl


db = TinyDB('.tmp/db.json')
tb = db.table('test66')

data_1 = {'int': 1, 'char': 'a'}
data_2 = {'name': 'Филиал "VODIY"', 'age': 330}
url = 'https://www.tutorialspoint.com/tinydb/tinydb_document_id.htm'

tb.insert(data_2)
# tb.update({'age': '66'})

# print(tb.all())
# print(db.all())


# SELLER_NAME = tb.search(where('var') == 'SELLER_NAME')[
# 0].get('SELLER_NAME')

# db.contains(doc_id = value)
# db.update({key : value}, doc_ids = […])
# db.update({'mark':'280'}, doc_ids = [4])
# db.remove(doc_ids = […])
# db.remove(doc_ids = [3,4])

Q = Query()
s_name2 = tb.search(where('name') == 'John5')
s_name = tb.search(Q.name == 'John5')
print(f'Result {s_name}')
print(f'Result2 {s_name2}')
# print(s_name2[0].get('name'))
print(tb.get(doc_id=1))


# db = TinydbCtrl(dbpath, 'test77')
# db.insert_data_into_tb(data_2)
# print(db.all())

# table = dbpath.table('ancient')
# table.insert(data_2)
# print(table.all())
