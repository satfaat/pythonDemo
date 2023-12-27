
import app.heroes.back.crud as crud
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, select
from typing import List
from app.heroes.back.models import Hero, HeroCreate, HeroRead, HeroUpdate
from app.features.database import get_session
from app.heroes.teams.teams import teams


heroes = FastAPI()
# heroes = APIRouter(
#     prefix='/api/heroes',
#     tags=["heroes"]
# )
heroes.include_router(teams)


@heroes.get("/", response_model=List[HeroRead])
def read_heroes(*,
                session: Session = Depends(get_session),
                skip: int = 0,
                limit: int = Query(default=100, le=100),
                ):
    heroes = crud.get_all(session, skip, limit)
    return heroes


@heroes.get("/{hero_id}", response_model=HeroRead)
def read_hero(*,
              session: Session = Depends(get_session),
              hero_id: int):
    hero = crud.get_by_id(session, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@heroes.post("/", response_model=HeroRead)
def create_hero(*,
                session: Session = Depends(get_session),
                hero: HeroCreate):
    return crud.create(session, hero)


@heroes.patch("/{hero_id}", response_model=HeroRead)
def update_hero(*,
                session: Session = Depends(get_session),
                hero_id: int,
                hero: HeroUpdate
                ):
    db_hero = session.get(Hero, hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero_data = hero.model_dump(exclude_unset=True)
    for key, value in hero_data.items():
        setattr(db_hero, key, value)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@heroes.delete("/{hero_id}")
def delete_hero(*,
                session: Session = Depends(get_session),
                hero_id: int):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}
