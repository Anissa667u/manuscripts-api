from fastapi import FastAPI
import app.routes.manuscript as manuscripts
import app.routes.ms_chapter as ms_chapter 

app = FastAPI(title = "Manuscript API")

app.include_router(manuscripts.router, prefix = "/manuscripts", tags = ["Manuscripts"])
app.include_router(ms_chapter.router, prefix = "/manuscript_chapters", tags = ["Manuscript_chapter"])
