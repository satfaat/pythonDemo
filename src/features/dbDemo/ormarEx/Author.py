import ormar
from src.dbDemo.ex_ormar.BaseMeta import BaseMeta


class Author(ormar.Model):
    class Meta(BaseMeta):
        tablename = "authors"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
