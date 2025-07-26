from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from app.models.post import Post
from app.models.user import User
from app.models.category import Category
from app.schemas.post import PostCreate, PostUpdate
from typing import Optional, List

async def get_post(db: AsyncSession, post_id: int) -> Optional[Post]:
    result = await db.execute(
        select(Post)
        .options(selectinload(Post.author), selectinload(Post.category), selectinload(Post.tags))
        .where(Post.id == post_id)
    )
    return result.scalar_one_or_none()

async def get_posts(db: AsyncSession, skip: int = 0, limit: int = 100, status: str = "published") -> List[Post]:
    query = select(Post).offset(skip).limit(limit)
    if status:
        query = query.where(Post.status == status)
    
    result = await db.execute(
        query.options(selectinload(Post.author), selectinload(Post.category), selectinload(Post.tags))
    )
    return result.scalars().all()

async def get_posts_by_author(db: AsyncSession, author_id: int, skip: int = 0, limit: int = 100) -> List[Post]:
    result = await db.execute(
        select(Post)
        .where(Post.author_id == author_id)
        .offset(skip)
        .limit(limit)
        .options(selectinload(Post.author), selectinload(Post.category), selectinload(Post.tags))
    )
    return result.scalars().all()

async def create_post(db: AsyncSession, post: PostCreate, author_id: int) -> Post:
    db_post = Post(
        title=post.title,
        content=post.content,
        excerpt=post.excerpt,
        slug=post.slug or post.title.lower().replace(" ", "-"),
        status=post.status,
        category_id=post.category_id,
        is_featured=post.is_featured,
        author_id=author_id
    )
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post

async def update_post(db: AsyncSession, post_id: int, post_update: PostUpdate) -> Optional[Post]:
    db_post = await get_post(db, post_id)
    if not db_post:
        return None
    
    update_data = post_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_post, key, value)
    
    await db.commit()
    await db.refresh(db_post)
    return db_post

async def delete_post(db: AsyncSession, post_id: int) -> bool:
    db_post = await get_post(db, post_id)
    if not db_post:
        return False
    
    await db.delete(db_post)
    await db.commit()
    return True

async def increment_view_count(db: AsyncSession, post_id: int) -> bool:
    db_post = await get_post(db, post_id)
    if not db_post:
        return False
    
    db_post.view_count += 1
    await db.commit()
    return True