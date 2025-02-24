from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to YouTube Transcripts API'}

def test_get_transcript_invalid_video():
    response = client.get('/api/v1/transcripts/invalid_video_id')
    assert response.status_code == 400