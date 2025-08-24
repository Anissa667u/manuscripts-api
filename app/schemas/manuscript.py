from pydantic import BaseModel

class MSAddSchema(BaseModel):
    title:str 
    author: str
    description: str
    
class MSSchema(MSAddSchema): 
    id: int 
    
    class Config:
        orm_mode = True 