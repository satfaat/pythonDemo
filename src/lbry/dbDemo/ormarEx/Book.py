import ormar
from typing import Optional
from src.dbDemo.ex_ormar.BaseMeta import BaseMeta
from src.dbDemo.ex_ormar.Author import Author


class Book(ormar.Model):
    class Meta(BaseMeta):
        tablename = "books"

    id: int = ormar.Integer(primary_key=True)
    author: Optional[Author] = ormar.ForeignKey(Author)
    title: str = ormar.String(max_length=100)
    year: int = ormar.Integer(nullable=True)
