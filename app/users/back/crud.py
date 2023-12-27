

from sqlmodel import Session, select
from app.users.back.models import User, UserCreate


def get_user(session: Session, user_id: int):
    return session.get(User, ident=user_id)


def get_user_by_email(session: Session, email: str):
    return session.get(User, email)


def get_users(
        session: Session,
        skip: int = 0,
        limit: int = 100):
    return session.exec(select(User).offset(skip).limit(limit)).all()


def create_user(session: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(
        email=user.email, hashed_password=fake_hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
