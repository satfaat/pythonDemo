

from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime
from sqlmodel import Field, Relationship, SQLModel
from app_alch.models.item import Item


class UserBase(SQLModel):
    username: str = Field(nullable=False)
    email: str = Field(unique=True, index=True)
    password: str = Field(nullable=False)
    is_active: bool = Field(default=True)


class User(UserBase, table=True):
    id: int = Field(primary_key=True, index=True)
    # items: Optional[Item] = Relationship(back_populates="owner")


class UserCreate(UserBase):
    ...


class UserPut(SQLModel):
    email: str
    password: str


class TokenBase(SQLModel):
    user_id: int
    refresh_token: str = Field(nullable=False)
    state: bool
    create_date: DateTime = Field(default=datetime.now)


class Token(TokenBase, table=True):
    access_token: str = Field(primary_key=True)


class TokenCreate(Token):
    ...


class TokenSchema(SQLModel):
    access_token: str
    refresh_token: str
