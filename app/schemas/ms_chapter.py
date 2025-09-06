from pydantic import BaseModel
import datetime

class MSAddChapter(BaseModel): #Валидация данных для глав
    chapter_title: str
    content: str 
    manuscript_id: int 
    date_of_publication: datetime.datetime 
    
class MS_chapter(MSAddChapter):
    chapter_id: int 
    class Config:
        orm_mode = True 