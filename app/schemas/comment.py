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

class PostResponseSimple(BaseModel):
    id: int
    title: str
    slug: str
    
    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    post_id: int
    author_name: Optional[str] = None
    author_email: Optional[str] = None
    author_url: Optional[str] = None
    content: str
    status: str = "pending"
    parent_id: Optional[int] = None

class CommentCreate(CommentBase):
    pass

class CommentUpdate(BaseModel):
    content: Optional[str] = None
    status: Optional[str] = None

class CommentResponse(CommentBase):
    id: int
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class CommentWithRelations(CommentResponse):
    author: Optional[UserResponseSimple] = None
    post: PostResponseSimple
    parent: Optional["CommentWithRelations"] = None
    replies: List["CommentWithRelations"] = []
    
    class Config:
        from_attributes = True

CommentWithRelations.model_rebuild()