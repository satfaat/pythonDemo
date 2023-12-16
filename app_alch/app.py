

from fastapi import FastAPI
from app_alch.routers.item import router as itemRoute
from app_alch.routers.user import router as userRoute
import app_alch.models.item as item
import app_alch.models.user as user
from configs.dbConf.sqlAlch import engine


app = FastAPI()
app.include_router(itemRoute)
app.include_router(userRoute)


@app.on_event("startup")
def on_startup() -> None:
    item.Base.metadata.create_all(bind=engine)
    user.Base.metadata.create_all(bind=engine)
