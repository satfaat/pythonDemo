from typing import List
from fastapi import APIRouter, HTTPException, status, Form
from fastapiDem.src.models.user import User, UserCreate, tb_users


router = APIRouter()


@router.get("/")
async def all() -> List[User]:
    return list(tb_users.all())


@router.get("/{id}")
async def get(id: int) -> User:
    try:
        return tb_users.get(doc_id=id)
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(user_create: UserCreate) -> User:
    user = User(**user_create.dict())
    tb_users.insert(user.dict())
    return user


@router.post("/submit/", response_model=User, status_code=status.HTTP_201_CREATED)
async def submit(nm: str = Form(...), pwd: str = Form(...)) -> User:
    user = User(first_name=None, last_name=None, username=nm,
                email=None, pwd=pwd).model_dump()
    tb_users.insert(user)
    return user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int) -> None:
    try:
        tb_users.remove(doc_ids=[id])
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
