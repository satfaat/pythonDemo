
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
import app_alch.crud.crud as crud
from app.features.database import get_session
from app.users.models import User, UserCreate


users = APIRouter(
    prefix='/api/users',
    tags=['users']
)


@users.post("/", response_model=User)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    db_user = crud.get_user_by_email(session, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=session, user=user)


@users.get("/", response_model=List[User])
def read_users(
        skip: int = 0,
        limit: int = 100,
        session: Session = Depends(get_session)):
    users = crud.get_users(session, skip=skip, limit=limit)
    return users


@users.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
