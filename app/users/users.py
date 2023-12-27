
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
import app_alch.crud.crud as crud
from app.features.database import get_session
from app.users.back.models import Token, TokenSchema, User, UserCreate, UserPut
from src.features.auth.token import create_access_token, create_refresh_token, get_hashed_password, verify_password


users = APIRouter(
    prefix='/api/users',
    tags=['users']
)


@users.get('/getusers')
def getusers(dependencies=Depends(JWTBearer()),
             session: Session = Depends(get_session)):
    user = session.exec(select(User)).all()
    return user

# @users.get("/", response_model=List[User])
# def read_users(
#         skip: int = 0,
#         limit: int = 100,
#         session: Session = Depends(get_session)):
#     users = crud.get_users(session, skip=skip, limit=limit)
#     return users


# @users.get("/{user_id}", response_model=User)
# def read_user(user_id: int, db: Session = Depends(get_session)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


@users.post("/register")
def register_user(user: UserCreate,
                  session: Session = Depends(get_session)):
    existing_user = session.exec(select(User).where(email=user.email))
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    encrypted_password = get_hashed_password(user.password)

    new_user = User(username=user.username,
                    email=user.email,
                    password=encrypted_password)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message": "user created successfully"}


@users.post("/", response_model=User)
def create_user(user: UserCreate,
                session: Session = Depends(get_session)):
    db_user = crud.get_user_by_email(session, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=session, user=user)


@users.post('/login', response_model=TokenSchema)
def login(request: UserPut,
          session: Session = Depends(get_session)):
    user = session.exec(select(User).where(
        User.email == request.email)).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect email")
    hashed_pass = user.password
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )

    access = create_access_token(user.id)
    refresh = create_refresh_token(user.id)

    token_db = Token(user_id=user.id,
                     access_toke=access,
                     refresh_toke=refresh,
                     state=True)
    session.add(token_db)
    session.commit()
    session.refresh(token_db)
    return {"access_token": access,
            "refresh_token": refresh}
