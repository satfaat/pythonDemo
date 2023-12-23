

from typing import Optional
from sqlmodel import Field, SQLModel


class TodoBase(SQLModel):
    task: str
    session_key: str


class Todo2(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
