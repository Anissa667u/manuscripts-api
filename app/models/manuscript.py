from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from sqlalchemy import Date, DateTime, ForeignKey 
import datetime

class ManuscriptModel(Base): # Это БД для хранения просто основной инфы про рукопись 
    __tablename__ = "manuscripts"
    id: Mapped[int] = mapped_column(primary_key= True)
    title: Mapped[str]
    author: Mapped[str]
    description: Mapped[str]
    
    chapters = relationship("MSchapterModel", back_populates="manuscript")
