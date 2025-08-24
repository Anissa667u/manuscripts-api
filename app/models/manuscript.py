from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class ManuscriptModel(Base):
    __tablename__ = "Manuscripts"
    id: Mapped[int] = mapped_column(primary_key= True)
    title: Mapped[str]
    author: Mapped[str]
    description: Mapped[str]
    
'''class MSchapterModel(ManuscriptModel):
    __tablename__ = "Manuscript's Chapter"
    chapter_id: Mapped[int] = mapped_column(primary_key=True)
    chapter_title: Mapped[str]
    date_of_publication: [date]'''