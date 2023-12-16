

from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from app_alch.models.item import Item


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = Field(default=True)


class User(UserBase, table=True):
    id: int = Field(primary_key=True, index=True)
    items: Optional[Item] = Relationship(back_populates="owner")


class UserCreate(UserBase):
    ...
