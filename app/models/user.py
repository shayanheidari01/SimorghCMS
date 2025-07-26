from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, Enum
from sqlalchemy.sql import func
from ..database import Base
from enum import Enum as PyEnum

class UserRole(str, PyEnum):
    ADMIN = "admin"
    EDITOR = "editor"
    AUTHOR = "author"
    CONTRIBUTOR = "contributor"
    SUBSCRIBER = "subscriber"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    role = Column(Enum(UserRole), default=UserRole.SUBSCRIBER)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    avatar_url = Column(String(255))
    bio = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"