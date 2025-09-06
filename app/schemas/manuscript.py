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

    