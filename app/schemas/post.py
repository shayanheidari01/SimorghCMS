from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserResponseSimple(BaseModel):
    id: int
    username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: str
    is_active: bool
    avatar_url: Optional[str] = None
    
    class Config:
        from_attributes = True

class CategoryResponse(BaseModel):
    id: int
    name: str
    slug: str
    description: Optional[str] = None
    
    class Config:
        from_attributes = True

class TagResponse(BaseModel):
    id: int
    name: str
    slug: str
    
    class Config:
        from_attributes = True

class CommentResponse(BaseModel):
    id: int
    author_name: Optional[str] = None
    author_email: Optional[str] = None
    content: str
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class PostBase(BaseModel):
    title: str
    content: Optional[str] = None
    excerpt: Optional[str] = None
    slug: Optional[str] = None
    status: str = "draft"
    category_id: Optional[int] = None
    is_featured: bool = False

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    author_id: int
    view_count: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    published_at: Optional[datetime] = None
    featured_image: Optional[str] = None
    
    class Config:
        from_attributes = True

class PostDetail(PostResponse):
    author: UserResponseSimple
    category: Optional[CategoryResponse] = None
    tags: List[TagResponse] = []
    comments: List[CommentResponse] = []
    
    class Config:
        from_attributes = True