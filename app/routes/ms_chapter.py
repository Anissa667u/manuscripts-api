from fastapi import APIRouter
from sqlalchemy import select 
from app.core.database import SessionDep, engine, Base 

from app.schemas.ms_chapter import MSAddChapter, MS_chapter
from app.models.ms_chapter import MSchapterModel 

router = APIRouter()


@router.post("/") #эндпоинт глав, дата публикаций генерируется автоматом в модели
async def add_ms_chapter(data:MSAddChapter, session:SessionDep):
    new_chapter = MSchapterModel (
        chapter_title = data.chapter_title, 
        content = data.content,
        manuscript_id = data.manuscript_id,
    )
    session.add(new_chapter)
    await session.commit()
    await session.refresh(new_chapter)
    
    return{
        "Ok": True,
        "Chapter_id": new_chapter.chapter_id,
        "Date_of_publication": new_chapter.date_of_publication.isoformat()
        }


@router.get("/")
async def get_ms_chapters(session:SessionDep):
    query = select(MSchapterModel)
    result = await session.execute(query)
    return result.scalars().all()
