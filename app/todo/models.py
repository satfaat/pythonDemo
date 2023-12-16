

from typing import Optional
from sqlmodel import Field, SQLModel


class TodoBase(SQLModel):
    task: str
    is_complete: bool


class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
