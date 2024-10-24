from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from typing import Optional, Union
from .models import User


'''ADD RECORD TO DATABASE'''
async def add(async_session: async_sessionmaker[AsyncSession], item: object) -> Optional[object]:
    async with async_session() as session:   
        session.add(item)   
        await session.commit()
        await session.refresh(item)
        await session.close()
        return item

'''DELETE RECORD FROM DATABASE'''
async def delete(async_session: async_sessionmaker[AsyncSession], item: object) -> Optional[object]:
    async with async_session() as session:
        session.delete(item)
        await session.commit()
        await session.refresh(item)
        await session.close()
        return item

async def getUserbyId(async_session: async_sessionmaker[AsyncSession], id: int) -> Optional[object]:
    async with async_session() as session:
        statement = select(User).filter_by(User.id == id)
        result = await session.execute(statement=statement)
        await session.close()
        return result.scalars().first()