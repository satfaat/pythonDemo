from typing import Dict
from fastapiDem.src.models.user import User
from fastapiDem.src.models.post import Post

# in memory db
class DummyDatabase:
    users: Dict[int, User] = {}
    posts: Dict[int, Post] = {}


db = DummyDatabase()
