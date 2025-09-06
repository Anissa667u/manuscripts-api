from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from sqlalchemy import Date, DateTime, ForeignKey 
import datetime


class MSchapterModel(Base): #Здесь хранится БД с главами, содержание и основная инфа 
    __tablename__ = "manuscript_chapters"
    chapter_id: Mapped[int] = mapped_column(primary_key=True)
    manuscript_id: Mapped[int] = mapped_column(ForeignKey("manuscripts.id")) #Связь с манускрипт 
    chapter_title: Mapped[str]  
    date_of_publication: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now(datetime.UTC)
        ) 
    content: Mapped[str]
    
    manuscript = relationship("ManuscriptModel", back_populates="chapters")
    comments = relationship("ChapterCommentsModel", back_populates="chapter")