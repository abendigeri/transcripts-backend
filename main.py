from fastapi import FastAPI
from app.routers import transcripts
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION
)

app.include_router(transcripts.router, prefix='/api/v1')

@app.get('/')
def read_root():
    return {'message': 'Welcome to YouTube Transcripts API'}
