from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from sqlalchemy import Date, DateTime, ForeignKey 
import datetime
    
class ChapterCommentsModel(Base):
    __tablename__ = "chapter_comments"
    comment_id: Mapped[int] = mapped_column(primary_key= True)
    content : Mapped[str]
    date_posted: Mapped[datetime.date] = mapped_column(Date)
    chapter_id: Mapped[int] = mapped_column(ForeignKey("manuscript_chapters.chapter_id"))  
    
    chapter = relationship("MSchapterModel", back_populates="comments") 