import pytest
from app.services.transcript_service import TranscriptService
from app.models.video import VideoTranscript
from datetime import datetime
import os

@pytest.fixture
def transcript_service():
    return TranscriptService()

@pytest.fixture
def sample_video_id():
    return 'sample_video_id'

@pytest.fixture
def mock_transcript_data():
    return [
        {'text': 'Hello', 'start': 0.0, 'duration': 1.0, 'language': 'en'},
        {'text': 'World', 'start': 1.0, 'duration': 1.0, 'language': 'en'}
    ]

def test_transcript_directory_creation(transcript_service):
    assert os.path.exists(transcript_service.transcripts_dir)

@pytest.mark.asyncio
async def test_save_transcript(transcript_service, sample_video_id):
    transcript = VideoTranscript(
        video_id=sample_video_id,
        title='Test Video',
        transcript_text='Test transcript',
        language='en',
        timestamp=datetime.now()
    )
    
    await transcript_service._save_transcript(transcript)
    
    file_path = os.path.join(transcript_service.transcripts_dir, f'{sample_video_id}.json')
    assert os.path.exists(file_path)