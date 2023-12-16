import ormar
from src.dbDemo.ex_ormar.config import metadata, database


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
