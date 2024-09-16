from sqlalchemy import select, update, delete, or_
from sqlalchemy.ext.asyncio import AsyncSession
from models import Users, Documents
from db.base import GetDB
from datetime import datetime
from typing import List, Optional
import re

async def upsert_user(chatid: int, username: Optional[str] = None) -> Users:
    async with GetDB() as db:
        stmt = select(Users).where(Users.chatid == chatid)
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()

        if user:
            stmt = update(Users).where(Users.chatid == chatid).values(
                last_online_at=datetime.utcnow(),
                username=username if username else Users.username
            )
            await db.execute(stmt)
        else:
            user = Users(chatid=chatid, username=username)
            db.add(user)

        await db.commit()
        await db.refresh(user)
        return user

async def create_document(title: str, description: str, tags: str, link: str, owner_chatid: int) -> Documents:
    async with GetDB() as db:
        document = Documents(title=title, description=description, tags=tags, link=link, owner_chatid=owner_chatid)
        db.add(document)
        await db.commit()
        await db.refresh(document)
        return document

async def update_document(doc_id: int, **kwargs) -> Optional[Documents]:
    async with GetDB() as db:
        stmt = update(Documents).where(Documents.id == doc_id).values(**kwargs)
        result = await db.execute(stmt)
        if result.rowcount > 0:
            await db.commit()
            stmt = select(Documents).where(Documents.id == doc_id)
            result = await db.execute(stmt)
            return result.scalar_one()
        return None

async def delete_document(doc_id: int) -> bool:
    async with GetDB() as db:
        stmt = delete(Documents).where(Documents.id == doc_id)
        result = await db.execute(stmt)
        if result.rowcount > 0:
            await db.commit()
            return True
        return False

async def find_similar_documents(text: str) -> List[Documents]:
    async with GetDB() as db:
        words = re.findall(r'\w+', text.lower())
        stmt = select(Documents).where(
            or_(*[Documents.tags.ilike(f'%{word}%') for word in words])
        )
        result = await db.execute(stmt)
        return result.scalars().all()

async def add_tags_to_document(doc_id: int, new_tags: List[str]) -> Optional[Documents]:
    async with GetDB() as db:
        stmt = select(Documents).where(Documents.id == doc_id)
        result = await db.execute(stmt)
        document = result.scalar_one_or_none()
        if document:
            existing_tags = set(tag.strip() for tag in document.tags.split(',')) if document.tags else set()
            updated_tags = existing_tags.union(new_tags)
            stmt = update(Documents).where(Documents.id == doc_id).values(tags=','.join(updated_tags))
            await db.execute(stmt)
            await db.commit()
            await db.refresh(document)
            return document
        return None

async def get_documents_by_tag(tag: str) -> List[Documents]:
    async with GetDB() as db:
        stmt = select(Documents).where(Documents.tags.ilike(f'%{tag}%'))
        result = await db.execute(stmt)
        return result.scalars().all()