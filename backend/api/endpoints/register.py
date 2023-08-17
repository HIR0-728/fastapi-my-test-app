import re

from api.db.db import session
from api.db.models.user import User
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="backend/api/templates")


@router.get("/register")
async def get_register(request: Request):
    return templates.TemplateResponse(
        "register.html", {"request": request, "username": "", "error": []}
    )


@router.post("/register")
async def post_register(request: Request):
    data = await request.form()
    username = data.get("username")
    password = data.get("password")
    password_tmp = data.get("password_tmp")
    email = data.get("email")

    error = []

    tmp_user = session.query(User).filter(User.username == username).first()
    pattern = re.compile(r"\w{4,20}")
    pattern_pw = re.compile(r"\w{6,20}")
    pattern_mail = re.compile(r"\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")

    if tmp_user is not None:
        error.append("そのユーザー名は既に使われています")
    if password != password_tmp:
        error.append("パスワードが一致しません")
    if pattern.match(username) is None:
        error.append("ユーザー名は4文字以上20文字以下の半角英数字で入力してください")
    if pattern_pw.match(password) is None:
        error.append("パスワードは6文字以上20文字以下の半角英数字で入力してください")
    if pattern_mail.match(email) is None:
        error.append("メールアドレスの形式が不正です")

    if error:
        return templates.TemplateResponse(
            "register.html", {"request": request, "username": username, "error": error}
        )

    user = User(username=username, password=password, email=email)
    session.add(user)
    session.commit()
    session.close()

    return templates.TemplateResponse(
        "complete.html", {"request": request, "username": username}
    )
