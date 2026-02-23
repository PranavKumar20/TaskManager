from fastapi import FastAPI
import app.db.model_init as _
from app.api.v1.api import api_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Collab Task API")
Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "API is running"}
