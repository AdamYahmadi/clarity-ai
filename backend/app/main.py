from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import documents, qa
from app.core.database import engine
from app.models import document as document_models

# Create the database tables on startup
document_models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Clarity AI API",
    description="Backend for the Clarity AI study assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(qa.router, prefix="/api/qa", tags=["Q&A"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Clarity AI API"}
