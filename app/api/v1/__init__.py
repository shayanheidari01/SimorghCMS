from fastapi import APIRouter
from . import auth, users, posts

api_v1_router = APIRouter()
api_v1_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_v1_router.include_router(users.router, prefix="", tags=["users"])
api_v1_router.include_router(posts.router, prefix="", tags=["posts"])