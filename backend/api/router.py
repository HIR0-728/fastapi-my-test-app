from api.endpoints import admin, register, test_api
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(test_api.router, prefix="", tags=["test"])
api_router.include_router(admin.router, prefix="", tags=["admin"])
api_router.include_router(register.router, prefix="", tags=["register"])
