

from fastapi import FastAPI


albums = FastAPI()
# albums = APIRouter(prefix="/api/albums",
#                    tags=["albums"])


@albums.get("/")
async def get_albums():
    return "pass"


@albums.get("/{id}")
async def get_album(id: int):
    return "pass"


@albums.post("/")
async def add_album(a1: album):
    return "pass"


@albums.put("/{id}")
async def update_album(id: int):
    return "pass"


@albums.delete("/{id}")
async def del_album(id: int):
    return "pass"
