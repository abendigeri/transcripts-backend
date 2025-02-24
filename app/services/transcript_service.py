import os
import json
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi
from app.core.config import settings
from app.models.video import VideoTranscript, VideoMetadata

class TranscriptService:
    def __init__(self):
        self.transcripts_dir = settings.TRANSCRIPTS_DIR
        os.makedirs(self.transcripts_dir, exist_ok=True)

    async def get_transcript(self, video_id: str) -> VideoTranscript:
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_text = ' '.join([item['text'] for item in transcript_list])
            
            # Get the first transcript's language
            language = transcript_list[0].get('language', 'en')
            
            # Create transcript object
            transcript = VideoTranscript(
                video_id=video_id,
                title=f'Video {video_id}',  # This would be updated with actual title
                transcript_text=transcript_text,
                language=language,
                timestamp=datetime.now()
            )
            
            # Save transcript to file
            await self._save_transcript(transcript)
            
            return transcript
        except Exception as e:
            raise Exception(f'Error getting transcript for video {video_id}: {str(e)}')

    async def _save_transcript(self, transcript: VideoTranscript):
        file_path = os.path.join(self.transcripts_dir, f'{transcript.video_id}.json')
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(transcript.dict(), f, default=str, ensure_ascii=False, indent=2)
        except Exception as e:
            raise Exception(f'Error saving transcript to file: {str(e)}')

    async def process_playlist(self, playlist_file: str):
        try:
            with open(playlist_file, 'r') as f:
                video_ids = [line.strip() for line in f if line.strip()]
            
            results = []
            for video_id in video_ids:
                try:
                    transcript = await self.get_transcript(video_id)
                    results.append({
                        'video_id': video_id,
                        'status': 'success',
                        'transcript': transcript
                    })
                except Exception as e:
                    results.append({
                        'video_id': video_id,
                        'status': 'error',
                        'error': str(e)
                    })
            
            return results
        except Exception as e:
            raise Exception(f'Error processing playlist file: {str(e)}')