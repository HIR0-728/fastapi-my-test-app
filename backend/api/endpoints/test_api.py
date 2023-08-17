from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="backend/api/templates")


@router.get("/test")
def test(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})
