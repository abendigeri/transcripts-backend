# YouTube Transcripts Backend

A FastAPI-based backend service for downloading and managing YouTube video transcripts. This service allows you to download transcripts from YouTube videos and playlists, storing them in a structured format for later use.

## Features

- Download transcripts from individual YouTube videos
- Process multiple videos from a playlist file
- Store transcripts in JSON format
- Store video metadata for database integration
- RESTful API endpoints for transcript management
- Unit test coverage
- MySQL database integration ready

## Technology Stack

- Python 3.8+
- FastAPI
- youtube-transcript-api
- MySQL Connector
- pytest for testing
- Docker support (optional)

## Project Structure

```
transcripts-backend/
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── video.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── transcripts.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── transcript_service.py
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_transcript_service.py
├── transcripts/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abendigeri/transcripts-backend.git
cd transcripts-backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create necessary directories:
```bash
mkdir transcripts
```

5. Create .env file with your configuration:
```bash
PROJECT_NAME="YouTube Transcripts Backend"
DATABASE_URL="mysql://user:password@localhost/db_name"
```

## Usage

1. Start the server:
```bash
uvicorn main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Get Transcript for Single Video
```http
GET /api/v1/transcripts/{video_id}
```

### Process Playlist File
```http
POST /api/v1/transcripts/process-playlist
```
Submit a file containing YouTube video IDs (one per line)

## Playlist File Format
Create a text file (playlist.txt) with YouTube video IDs, one per line:
```
dQw4w9WgXcQ
jNQXAC9IVRw
```

## Running Tests
```bash
pytest
```

## Data Storage

### Transcript Storage
Transcripts are stored in JSON format in the `transcripts/` directory with the following structure:
```json
{
  "video_id": "string",
  "title": "string",
  "transcript_text": "string",
  "language": "string",
  "timestamp": "datetime"
}
```

### Video Metadata Structure
Video metadata is structured for MySQL database storage with the following fields:
- video_id (PRIMARY KEY)
- title
- description
- channel_id
- channel_title
- published_at
- view_count
- like_count
- duration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.