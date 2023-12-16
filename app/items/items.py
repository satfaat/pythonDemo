
import app.items.crud as crud
from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.features.database import get_session
from app.items.models import Item, ItemCreate


items = APIRouter(
    prefix='/api/items',
    tags=['items']
)


@items.get("/", response_model=List[Item])
def read_items(
        skip: int = 0,
        limit: int = 100,
        session: Session = Depends(get_session)):
    items = crud.get_items(session, skip=skip, limit=limit)
    return items


@items.post("/{user_id}/items/", response_model=Item)
def create_item_for_user(user_id: int,
                         item: ItemCreate,
                         session: Session = Depends(get_session)
                         ):
    return crud.create_user_item(session, item, user_id)
