from pydantic import BaseModel
from fastapiDem.configs.config import tinydb

tb_users = tinydb.table('Users')


class UserCreate(BaseModel):
    first_name: str | None
    last_name: str | None
    username: str
    email: str | None
    pwd: str


class User(BaseModel):
    first_name: str | None
    last_name: str | None
    username: str
    email: str | None
    pwd: str
