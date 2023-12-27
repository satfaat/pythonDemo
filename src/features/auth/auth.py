

import jwt
import secrets
from fastapi.security import HTTPBasic
from pydantic import BaseModel

# globals
basic_auth = HTTPBasic(auto_error=False)
auth_cookie_name = "reminders_session"


class AuthCookie(BaseModel):
    name: str
    token: str
    username: str


def serialize_token(username: str) -> str:
    return jwt.encode({"username": username}, secret_key, algorithm="HS256")


def deserialize_token(token: str) -> str:
    try:
        data = jwt.decode(token, secret_key, algorithms=["HS256"])
        return data['username']
    except:
        return None
