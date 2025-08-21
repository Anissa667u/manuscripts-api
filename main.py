from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from pydantic import BaseModel
from typing import Annotated 
from sqlalchemy import select 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = FastAPI()

#настраиваем все что надо для бд 
engine = create_async_engine('sqlite+aiosqlite:///manuscripts.db')
new_session = async_sessionmaker(engine, expire_on_commit= False)
async def get_session():
    async with new_session() as session:
        yield session
        
SessionDep = Annotated[AsyncSession, Depends(get_session)]

class Base(DeclarativeBase):
    pass 

class ManuscriptModel(Base):
    __tablename__ = "Manuscripts"
    id: Mapped[int] = mapped_column(primary_key= True)
    title: Mapped[str]
    author: Mapped[str]
    description: Mapped[str]

@app.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok": True}

class MSAddSchema(BaseModel):
    title:str 
    author: str
    description: str
    
class MSSchema(MSAddSchema): 
    id: int 
    
@app.post("/manuscripts")
async def add_ms(data: MSAddSchema, session: SessionDep):
    new_manuscript = ManuscriptModel (
        title = data.title,
        author = data.author,
        description = data.description,
    )
    session.add(new_manuscript)
    await session.commit()
    return {"Ok": True}
    
@app.get("/manuscripts")
async def get_ms(session: SessionDep):
    query = select(ManuscriptModel)
    result = await session.execute(query)
    return result.scalars().all()