import hashlib

from api.auth import auth
from api.db.db import session
from api.db.models.task import Task
from api.db.models.user import User
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_401_UNAUTHORIZED

router = APIRouter()
templates = Jinja2Templates(directory="backend/api/templates")


@router.get("/admin")
def admin(
    request: Request,
    credentials: HTTPBasicCredentials = Depends(HTTPBasic()),
):
    username = auth(credentials)
    password = hashlib.md5(credentials.password.encode()).hexdigest()

    user = session.query(User).filter(User.username == username).first()
    tasks = (
        session.query(Task).filter(Task.user_id == user.id).all()
        if user is not None
        else []
    )
    session.close()

    # ユーザーがいない場合
    if user is None or user.password != password:
        error = "ユーザー名かパスワードが間違っています"

        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail=error,
            headers={"WWW-Authenticate": "Basic"},
        )
    return templates.TemplateResponse(
        "admin.html", {"request": request, "user": user, "task": tasks}
    )
