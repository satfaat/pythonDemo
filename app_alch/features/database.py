

from sqlmodel import SQLModel, Session
from configs.configDB import engine


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
