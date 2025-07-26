from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

# Association table for post-tag relationship
post_tag = Table(
    'post_tag',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True, nullable=False)
    content = Column(Text)
    excerpt = Column(Text)
    featured_image = Column(String(255))
    status = Column(String(20), default="draft")  # draft, published, private
    author_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    view_count = Column(Integer, default=0)
    is_featured = Column(Boolean, default=False)
    published_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    author = relationship("User", back_populates="posts")
    category = relationship("Category", back_populates="posts")
    tags = relationship("Tag", secondary=post_tag, back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    
    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}', status='{self.status}')>"

# Update User model to include relationship
from .user import User
User.posts = relationship("Post", back_populates="author")