

from sqlmodel import Session, select
from app.items.models import Item, ItemCreate


def get_items(session: Session, skip: int = 0, limit: int = 100):
    return session.exec(select(Item).offset(skip).limit(limit)).all()


def create_user_item(session: Session, item: ItemCreate, user_id: int):
    db_item = Item(**item.model_dump(), owner_id=user_id)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item
