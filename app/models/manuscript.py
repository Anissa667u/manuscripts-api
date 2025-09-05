from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from sqlalchemy import Date, DateTime 
import datetime

class ManuscriptModel(Base):
    __tablename__ = "Manuscripts"
    id: Mapped[int] = mapped_column(primary_key= True)
    title: Mapped[str]
    author: Mapped[str]
    description: Mapped[str]
    
class MSchapterIDModel(ManuscriptModel):
    __tablename__ = "Manuscript's Chapter"
    chapter_id: Mapped[int] = mapped_column(primary_key=True)
    comments: ....

class MSChapterModel(MSchapterIDModel)
    chapter_title: Mapped[str]  
    date_of_publication: Mapped[datetime.datetime] = mapped_column(DateTime) 
    content: Mapped[str]
    

class ChapterCommentsModel(MSchapterIDModel):
    __tablename__ = "Comments for chapter"
    comment_id: Mapped[int] = mapped_column(primary_key= True)
    content : Mapped[str]
    date_posted: Mapped[datetime.date] = mapped_column(Date)
    chapter_id: Mapped[int] = mapped_column(ForeignKey("chapters.chapter_id"))    
    