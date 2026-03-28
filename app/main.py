from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.db.model_init as _
from app.api.v1.api import api_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Collab Task API")

# --- CORS CONFIGURATION ---
# This allows your Vite frontend (running on port 5173) to talk to this API
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allows all headers (important for your JWT)
)
# ---------------------------

Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "API is running"}
