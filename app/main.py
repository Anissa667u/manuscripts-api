from fastapi import FastAPI
import app.routes.manuscript as manuscripts
import app.routes.ms_chapter as ms_chapter 
from app.core.database import engine, Base 


app = FastAPI(title = "Manuscript API")

@app.post("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(manuscripts.router, prefix = "/manuscripts", tags = ["Manuscripts"])
app.include_router(ms_chapter.router, prefix = "/manuscript_chapters", tags = ["Manuscript_chapter"])
