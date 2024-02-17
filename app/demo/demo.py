

from typing import Annotated
from fastapi import Body, Depends, FastAPI, Header
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


demo = FastAPI()


@demo.get("/")
def home():
    return {"demo": "you are in demo page"}


@demo.get("/data")
def data(who):
    return f"Call {who}?"


# @demo.post("/data")
# def data(who: str = Body(embed=True)):
#     return f"Call {who}?"


@demo.post("/data")
def data(who: str = Header()):
    return f"Call {who}?"


@demo.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! You don't need to be "
                "authenticated to see this.")
    }
    return result


@demo.get("/api/private")
def private(token: Annotated[str, Depends(oauth2_scheme)]):
    """A valid access token is required to access this route"""

    result = {"token": token}

    return result
