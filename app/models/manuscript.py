from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from sqlalchemy import Date, DateTime, ForeignKey 
import datetime

class ManuscriptModel(Base): # Это БД для хранения просто основной инфы про рукопись 
    __tablename__ = "Manuscripts"
    id: Mapped[int] = mapped_column(primary_key= True)
    title: Mapped[str]
    author: Mapped[str]
    description: Mapped[str]
    
class MSchapterIDModel(ManuscriptModel): #Здесь хранится БД с главами, содержание и основная инфа 
    __tablename__ = "Manuscript_chapter"
    chapter_id: Mapped[int] = mapped_column(primary_key=True)
    chapter_title: Mapped[str]  
    date_of_publication: Mapped[datetime.datetime] = mapped_column(DateTime) 
    content: Mapped[str]
    
class ChapterCommentsModel(MSchapterIDModel):
    __tablename__ = "Chapter_comments"
    comment_id: Mapped[int] = mapped_column(primary_key= True)
    content : Mapped[str]
    date_posted: Mapped[datetime.date] = mapped_column(Date)
    chapter_id: Mapped[int] = mapped_column(ForeignKey("Manuscript_chapter.chapter_id"))    
    