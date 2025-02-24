from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class VideoTranscript(BaseModel):
    video_id: str
    title: str
    transcript_text: str
    language: str
    timestamp: datetime

class VideoMetadata(BaseModel):
    video_id: str
    title: str
    description: Optional[str] = None
    channel_id: Optional[str] = None
    channel_title: Optional[str] = None
    published_at: Optional[datetime] = None
    view_count: Optional[int] = None
    like_count: Optional[int] = None
    duration: Optional[str] = None

class PlaylistItem(BaseModel):
    video_id: str
    title: str
    position: int
    playlist_id: str