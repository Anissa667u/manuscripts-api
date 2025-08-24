from fastapi import FastAPI
import app.routes.manuscript as manuscripts

app = FastAPI(title = "Manuscript API")
app.include_router(manuscripts.router, prefix = "/manuscripts", tags = ["Manuscripts"])
