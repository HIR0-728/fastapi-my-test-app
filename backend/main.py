from api import router
from fastapi import FastAPI
from starlette.templating import Jinja2Templates


def create_templates():
    templates = Jinja2Templates(directory="templates")
    return templates


def create_application():
    app = FastAPI(
        title="My Test Application",
        description="This is sample application",
        version="0.0.1",
    )
    app.include_router(router.api_router, prefix="/api")
    return app


app = create_application()


@app.get("/hc")
def health_check():
    return {"status": "ok"}
