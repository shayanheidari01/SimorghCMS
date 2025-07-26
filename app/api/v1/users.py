from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app import crud
from app.database import get_db
from app.api.deps import get_current_active_user, get_current_admin
from app.schemas.user import UserResponse, UserWithPosts, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserResponse])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_admin)
):
    users = await crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/me", response_model=UserResponse)
async def read_users_me(
    current_user: UserResponse = Depends(get_current_active_user)
):
    return current_user

@router.get("/{user_id}", response_model=UserWithPosts)
async def read_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_active_user)
):
    user = await crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/me", response_model=UserResponse)
async def update_user_me(
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_active_user)
):
    user = await crud.update_user(db, user_id=current_user.id, user_update=user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_admin)
):
    user = await crud.update_user(db, user_id=user_id, user_update=user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_admin)
):
    if user_id == current_user.id:
        raise HTTPException(status_code=400, detail="You cannot delete yourself")
    
    success = await crud.delete_user(db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": "User deleted successfully"}