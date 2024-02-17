
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from app.site.configFastapi import templates
from src.features.web.reader import open_json, open_md


site = FastAPI(
    tags=['page']
)
# site.mount('/static', StaticFiles(directory='site/front/static'), name='static')
