from fastapi import APIRouter
from sqlalchemy import select 
from app.core.database import SessionDep, engine, Base 
from app.models.manuscript import ManuscriptModel
from app.schemas.manuscript import MSSchema, MSAddSchema 


router = APIRouter()


'''@router.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok": True} '''

@router.post("/")
async def add_ms(data: MSAddSchema, session: SessionDep):
    new_manuscript = ManuscriptModel (
        title = data.title,
        author = data.author,
        description = data.description,
    )
    session.add(new_manuscript)
    await session.commit()
    return {"Ok": True}

@router.get("/")
async def get_manuscripts(session: SessionDep):
    query = select(ManuscriptModel)
    result = await session.execute(query)
    return result.scalars().all()
