# Architecture Overview

## Modules
- **camera.py:** Captures live video feed from the iPhone (via QuickTime).
- **detection.py:** Implements object detection using YOLOv8.
- **ocr.py:** Applies OCR to extract license plate information.
- **reid.py:** Performs clothing-color based person re-identification.
- **notification.py:** Sends notifications via LINE API.

## Data Flow
1. **Video Capture:** `camera.py` fetches frames from the live feed.
2. **Detection:** Each frame is processed by `detection.py` to detect objects.
3. **OCR & Re-ID:** Detected vehicles are processed in `ocr.py` and persons in `reid.py`.
4. **Event Handling:** Events (detections) are logged, snapshots saved to `data/`, and notifications sent via `notification.py`.
