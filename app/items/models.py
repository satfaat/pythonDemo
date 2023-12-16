

from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from app.users.models import User


class ItemBase(SQLModel):
    title: str = Field(index=True)
    description: Optional[str] = Field(default=None, index=True)

    owner_id: Optional[int] = Field(default=None, foreign_key="users.id")


class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner: Optional[User] = Relationship(back_populates="items")


class ItemCreate(ItemBase):
    ...
