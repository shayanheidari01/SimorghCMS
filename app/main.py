from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.api.v1 import api_v1_router
from app.database import engine, Base
from app.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files - اصلاح شده
if not os.path.exists("static"):
    os.makedirs("static")

# Mount static files for both uploads and frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(api_v1_router, prefix="/api/v1")

# Serve frontend files - اصلاح شده
@app.get("/")
async def serve_frontend():
    return FileResponse("static/frontend/index.html")

@app.get("/posts")
async def serve_posts():
    return FileResponse("static/frontend/posts.html")

@app.get("/posts/{post_id}")
async def serve_post_detail(post_id: int):
    return FileResponse("static/frontend/post.html")

@app.get("/login")
async def serve_login():
    return FileResponse("static/frontend/login.html")

@app.get("/register")
async def serve_register():
    return FileResponse("static/frontend/register.html")

@app.get("/dashboard")
async def serve_dashboard():
    return FileResponse("static/frontend/dashboard.html")

@app.get("/profile")
async def serve_profile():
    return FileResponse("static/frontend/profile")

# برای سرو کردن فایل‌های استاتیک فرانت‌اند
@app.get("/css/{file_path:path}")
async def serve_css(file_path: str):
    file_path = f"static/frontend/css/{file_path}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return FileResponse("static/frontend/index.html")

@app.get("/js/{file_path:path}")
async def serve_js(file_path: str):
    file_path = f"static/frontend/js/{file_path}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return FileResponse("static/frontend/index.html")

@app.get("/images/{file_path:path}")
async def serve_images(file_path: str):
    file_path = f"static/frontend/images/{file_path}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return FileResponse("static/frontend/index.html")

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}