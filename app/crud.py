from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from typing import Optional, Union

class CRUD():
    '''ADD RECORD TO DATABASE'''
    async def add(self, async_session: async_sessionmaker[AsyncSession], item: object) -> Optional[object]:
        async with async_session() as session:   
            session.add(item)   
            await session.commit()
            await session.refresh(item)
            await session.close()
            return item

    '''DELETE RECORD FROM DATABASE'''
    async def delete(self, async_session: async_sessionmaker[AsyncSession], item: object) -> Optional[object]:
        async with async_session() as session:
            session.delete(item)
            await session.commit()
            await session.refresh(item)
            await session.close()
            return item
        
