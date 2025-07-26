from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    author_name = Column(String(100))
    author_email = Column(String(100))
    author_url = Column(String(255))
    content = Column(Text, nullable=False)
    status = Column(String(20), default="pending")  # pending, approved, spam, trash
    parent_id = Column(Integer, ForeignKey("comments.id"))
    ip_address = Column(String(45))
    user_agent = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    post = relationship("Post", back_populates="comments")
    parent = relationship("Comment", remote_side=[id], back_populates="replies")
    replies = relationship("Comment", back_populates="parent")
    author = relationship("User", back_populates="comments")
    author_id = Column(Integer, ForeignKey("users.id"))
    
    def __repr__(self):
        return f"<Comment(id={self.id}, post_id={self.post_id})>"

# Update User model to include relationship
from .user import User
User.comments = relationship("Comment", back_populates="author")