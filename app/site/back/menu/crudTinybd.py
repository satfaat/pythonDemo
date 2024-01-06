
from fastapi import HTTPException, status
from configs.dbConf.tinyDbConf import tb_menu_1
# from fastapiDem.src.models.user import User, UserCreate


def get_all_records():
    return list(tb_menu_1.all())


# def get_by_id(id: int):
#     try:
#         return tb_menu_1.get(doc_id=id)
#     except KeyError:
#         raise HTTPException(status.HTTP_404_NOT_FOUND)


# def create(user_create: UserCreate):
#     user_db = User(**user_create.dict())
#     tb_menu_1.insert(user_db.dict())
#     return user_db


# def create_with_form(nm, pwd):
#     user = User(first_name=None, last_name=None, username=nm,
#                 email=None, pwd=pwd).model_dump()
#     tb_menu_1.insert(user)
#     return user


# def delete_record_by_id(id: int):
#     try:
#         tb_menu_1.remove(doc_ids=[id])
#     except KeyError:
#         raise HTTPException(status.HTTP_404_NOT_FOUND)
