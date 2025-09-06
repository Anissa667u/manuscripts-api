from pydantic import BaseModel
import datetime

class MSAddSchema(BaseModel):
    title:str 
    author: str
    description: str
    
class MSSchema(MSAddSchema): 
    id: int 
    
    class Config:
        orm_mode = True 
        
class MSAddChapter(BaseModel): #Валидация данных для глав
    chapter_title: str
    content: str 
    manuscript_id: int 
    date_of_publication: datetime.datetime 
    
class MS_chapter(MSAddChapter):
    chapter_id: int 
    class Config:
        orm_mode = True 
        
class MSAddChapterComment(BaseModel):
    content: str
    chapter_id: int 
    
class MSChapterComment(MSAddChapterComment):
    date_posted: datetime 
    comment_id:int 
    class Config:
        orm_mode = True
    
    