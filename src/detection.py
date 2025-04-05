# This is a simplified example using YOLOv8 via ultralytics package
from ultralytics import YOLO
import cv2

class Detector:
    def __init__(self, model_path, conf_threshold=0.5):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold

    def detect(self, frame):
        results = self.model(frame)
        detections = []
        for result in results:
            for pred in result.boxes.data.tolist():
                x1, y1, x2, y2, conf, cls = pred
                if conf < self.conf_threshold:
                    continue
                label = self.model.model.names[int(cls)]
                bbox = [int(x1), int(y1), int(x2 - x1), int(y2 - y1)]
                detections.append({"label": label, "bbox": bbox, "confidence": conf})
        return detections
