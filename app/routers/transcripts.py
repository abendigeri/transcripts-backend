from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.transcript_service import TranscriptService
from app.models.video import VideoTranscript
from typing import List
import tempfile
import os

router = APIRouter(prefix='/transcripts', tags=['transcripts'])
transcript_service = TranscriptService()

@router.get('/{video_id}', response_model=VideoTranscript)
async def get_transcript(video_id: str):
    try:
        return await transcript_service.get_transcript(video_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post('/process-playlist', response_model=List[dict])
async def process_playlist(playlist_file: UploadFile = File(...)):
    try:
        # Create a temporary file to store the uploaded content
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            content = await playlist_file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name

        # Process the playlist
        try:
            results = await transcript_service.process_playlist(temp_file_path)
        finally:
            # Clean up the temporary file
            os.unlink(temp_file_path)

        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))