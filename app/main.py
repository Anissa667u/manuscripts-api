from fastapi import FastAPI
from app.routes import manuscripts

app = FastApi(title = "Manuscript API")
app.include_router(manuscripts.app, prefix = "/manuscripts", tags = [manuscripts])