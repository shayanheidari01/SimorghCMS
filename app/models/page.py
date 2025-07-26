from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

class Page(Base):
    __tablename__ = "pages"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True, nullable=False)
    content = Column(Text)
    excerpt = Column(Text)
    featured_image = Column(String(255))
    status = Column(String(20), default="draft")  # draft, published, private
    author_id = Column(Integer, ForeignKey("users.id"))
    parent_id = Column(Integer, ForeignKey("pages.id"))
    menu_order = Column(Integer, default=0)
    template = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    author = relationship("User", back_populates="pages")
    parent = relationship("Page", remote_side=[id], back_populates="children")
    children = relationship("Page", back_populates="parent")
    
    def __repr__(self):
        return f"<Page(id={self.id}, title='{self.title}')>"

# Update User model to include relationship
from .user import User
User.pages = relationship("Page", back_populates="author")