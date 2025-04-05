import cv2
import yaml
import os
import time
from camera import Camera
from detection import Detector
from ocr import OCR
from reid import reidentify_person
from notification import send_line_notification

# Load configuration
with open("../config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Create necessary directories if they don't exist
os.makedirs(config["logging"]["snapshot_dir"], exist_ok=True)
os.makedirs(config["logging"]["log_dir"], exist_ok=True)

def log_event(event_info, snapshot):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    log_path = os.path.join(config["logging"]["log_dir"], f"log_{timestamp}.txt")
    with open(log_path, "w") as log_file:
        log_file.write(event_info)
    snapshot_path = os.path.join(config["logging"]["snapshot_dir"], f"snapshot_{timestamp}.jpg")
    cv2.imwrite(snapshot_path, snapshot)
    return snapshot_path

def main():
    # Initialize modules
    camera = Camera(source=config["camera"]["source"])
    detector = Detector(model_path=config["detection"]["model_path"],
                        conf_threshold=config["detection"]["conf_threshold"])
    ocr_engine = OCR(tesseract_cmd=config["ocr"]["tesseract_cmd"])

    cap = camera.start_capture()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run object detection
        detections = detector.detect(frame)

        for det in detections:
            # Example: det could be a dict with keys: 'label', 'bbox', 'confidence'
            label = det["label"]
            bbox = det["bbox"]  # (x, y, w, h)

            # Draw bounding box around the detected object
            cv2.rectangle(frame, (bbox[0], bbox[1]),
                          (bbox[0] + bbox[2], bbox[1] + bbox[3]),
                          (0, 255, 0), 5)

            # Overlay the label above the bounding box
            cv2.putText(
                frame, label, (bbox[0], bbox[1] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            if label == "vehicle":
                # Crop the region for OCR processing
                vehicle_img = frame[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
                plate_text = ocr_engine.extract_text(vehicle_img)
                det["plate"] = plate_text
            elif label == "person":
                # Run re-identification (clothing-color based)
                person_id = reidentify_person(frame, bbox)
                det["person_id"] = person_id

            # Log event and notify if necessary
            event_info = f"Detected {label} with details: {det}"
            snapshot_path = log_event(event_info, frame)
            send_line_notification(event_info, snapshot_path, config["notification"]["line_notify_token"])

        cv2.imshow("Securi-Tea-Time", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
