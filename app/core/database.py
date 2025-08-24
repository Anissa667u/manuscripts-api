from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated
from fastapi import Depends

#настраиваем все что надо для бд 
engine = create_async_engine('sqlite+aiosqlite:///manuscripts.db')
new_session = async_sessionmaker(engine, expire_on_commit= False)


async def get_session():
    async with new_session() as session:
        yield session
        
SessionDep = Annotated[AsyncSession, Depends(get_session)]

class Base(DeclarativeBase):
    pass 
