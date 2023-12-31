from typing import List
from fastapi import APIRouter, HTTPException, status
from fastapiDem.src.models.post import Post, PostCreate
from fastapiDem.src.db import db


router = APIRouter(
    prefix='/posts',
    tags=["posts"]
)


@router.get("/")
async def all() -> List[Post]:
    return list(db.posts.values())


@router.get("/{id}")
async def get(id: int) -> Post:
    try:
        return db.posts[id]
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(post_create: PostCreate) -> Post:
    try:
        db.users[post_create.user]
    except KeyError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=f"User with id {post_create.user} doesn't exist.",
        )

    new_id = max(db.posts.keys() or (0,)) + 1
    post = Post(id=new_id, **post_create.model_dump())
    db.posts[new_id] = post
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int) -> None:
    try:
        db.posts.pop(id)
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
