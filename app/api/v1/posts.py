from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app import crud
from app.database import get_db
from app.api.deps import get_current_active_user
from app.schemas.post import PostCreate, PostUpdate, PostResponse, PostDetail
from app.schemas.user import UserResponse

router = APIRouter(prefix="/posts", tags=["posts"])

@router.get("/", response_model=List[PostResponse])
async def read_posts(
    skip: int = 0,
    limit: int = 100,
    status: str = Query("published", description="Filter by status"),
    db: AsyncSession = Depends(get_db)
):
    posts = await crud.get_posts(db, skip=skip, limit=limit, status=status)
    return posts

@router.get("/{post_id}", response_model=PostDetail)
async def read_post(
    post_id: int,
    db: AsyncSession = Depends(get_db)
):
    post = await crud.get_post(db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Increment view count
    await crud.increment_view_count(db, post_id)
    return post

@router.post("/", response_model=PostResponse)
async def create_post(
    post: PostCreate,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_active_user)
):
    return await crud.create_post(db=db, post=post, author_id=current_user.id)

@router.put("/{post_id}", response_model=PostResponse)
async def update_post(
    post_id: int,
    post: PostUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_active_user)
):
    db_post = await crud.get_post(db, post_id=post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if db_post.author_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    return await crud.update_post(db=db, post_id=post_id, post_update=post)

@router.delete("/{post_id}")
async def delete_post(
    post_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_active_user)
):
    db_post = await crud.get_post(db, post_id=post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if db_post.author_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    success = await crud.delete_post(db=db, post_id=post_id)
    if not success:
        raise HTTPException(status_code=500, detail="Could not delete post")
    
    return {"message": "Post deleted successfully"}