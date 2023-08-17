import hashlib

from api.db.db import session
from api.db.models.user import User
from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED


def auth(credentials):
    username = credentials.username
    password = hashlib.md5(credentials.password.encode()).hexdigest()

    user = session.query(User).filter(User.username == username).first()
    session.close()

    if user is None or user.password != password:
        error = "ユーザー名かパスワードが間違っています"
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail=error,
            headers={"WWW-Authenticate": "Basic"},
        )
    return username
