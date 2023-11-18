from fastapi.templating import Jinja2Templates
from tinydb import TinyDB


tinydb = TinyDB('.dbs/dto.json')
templates = Jinja2Templates(directory='./templates')
