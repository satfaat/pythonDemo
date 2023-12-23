from fastapi import HTTPException
from sqlmodel import Session, select
from app.todo2.back.models import Todo2


def get_all(
        session: Session,
        session_key: str,
        skip: int = 0,
        limit: int = 100):
    return session.exec(select(Todo2)
                        .where(Todo2.session_key == session_key)
                        .offset(skip).limit(limit)).all()


def get_by_id(session: Session, todo_id: int):
    return session.get(Todo2, todo_id)


def create(session: Session,
           task: str,
           session_key: str):
    todo = Todo2(task=task, session_key=session_key)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


def update_by_id(session: Session,
                 todo_id: int,
                 task: str):
    todo = get_by_id(session, todo_id)
    todo.task = task
    session.commit()
    session.refresh(todo)
    return todo


def delete_by_id(session: Session,
                 todo_id: int):
    todo = get_by_id(session, todo_id)
    if not todo:
        raise HTTPException(404, "Task not found")
    session.delete(todo)
    session.commit()
