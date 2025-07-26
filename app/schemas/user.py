from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: str = "subscriber"
    is_active: bool = True
    bio: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(UserBase):
    password: Optional[str] = Field(None, min_length=8)

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    avatar_url: Optional[str] = None
    
    class Config:
        from_attributes = True

class UserWithPosts(UserResponse):
    # این فیلدها بعداً اضافه می‌شوند وقتی مدل‌ها کامل شدند
    posts: List = []
    comments: List = []
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None