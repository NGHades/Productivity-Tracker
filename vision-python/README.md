# Phase 1: Python Vision Service

Computer vision service that detects human actions and provides REST API endpoints.

## Features

- **Webcam Capture**: OpenCV VideoCapture pipeline
- **AI Detection**: MediaPipe integration for pose, face mesh, and hands
- **Action Classification**: Maps pose/hand/eye data to productivity actions
- **REST API**: FastAPI service with endpoints for real-time analysis
- **Testing**: Unit tests for the vision pipeline

## Quick Setup

```bash
# Install dependencies
chmod +x ../setup/phase1-install.sh
../setup/phase1-install.sh

# Or manual install:
cd vision-python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Start the Service
```bash
cd vision-python
source venv/bin/activate
python main.py
```

### API Endpoints
- `POST /start` - Begin webcam capture
- `POST /stop` - Stop capture
- `GET /analyze` - Return action JSON per frame

### Testing
```bash
# Run tests
pytest

# Test with sample data
python -m pytest tests/ -v
```

## Development Tasks

### ✅ Completed
- [ ] Webcam capture pipeline (OpenCV VideoCapture)
- [ ] Frame reading and display testing
- [ ] MediaPipe integration (Pose, Face Mesh, Hands)
- [ ] Head angle, eye direction, hand position extraction
- [ ] Action classification logic with confidence scoring
- [ ] FastAPI REST service setup
- [ ] Unit tests for Python pipeline
- [ ] Sample video testing
- [ ] JSON output verification

### 📊 Expected Output
```json
{
  "timestamp": "2025-12-02T10:30:00Z",
  "actions": [
    {
      "type": "typing",
      "confidence": 0.85,
      "hand_position": {"x": 0.5, "y": 0.3},
      "head_angle": {"pitch": 15, "yaw": 0, "roll": 2}
    }
  ],
  "pose_landmarks": {...},
  "face_mesh": {...}
}
```