
from sqlmodel import Session, select
from app.todo.models import Todo


def get_all(
        session: Session,
        skip: int = 0,
        limit: int = 100):
    return session.exec(select(Todo).offset(skip).limit(limit)).all()


def get_by_id(session: Session, todo_id: int):
    return session.get(Todo, todo_id)


# def create(session: Session,
#            hero: HeroCreate):
#     db_hero = Hero.model_validate(hero)
#     session.add(db_hero)
#     session.commit()
#     session.refresh(db_hero)
#     return db_hero
