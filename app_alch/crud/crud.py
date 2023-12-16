from sqlalchemy.orm import Session
from app_alch.models.item import Item as ModelItem
from app_alch.models.user import User as ModelUser
from app_alch.schemas.item import ItemCreate
from app_alch.schemas.user import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(ModelUser).filter(ModelUser.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(ModelUser).filter(ModelUser.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ModelUser).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = ModelUser(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ModelItem).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = ModelItem(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
