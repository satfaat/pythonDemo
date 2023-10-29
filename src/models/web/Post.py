from typing import TypedDict
from pydantic import BaseModel, Field
from utils.fakers import random_string


class Post(BaseModel):
    title: str = Field(default_factory=random_string)
    body: str = Field(default_factory=random_string)
    user_id: int = Field(
        alias='userId',
        default_factory=1
    )


print(Post().dict(by_alias=True))
