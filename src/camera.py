import cv2

class Camera:
    def __init__(self, source=0):
        self.source = source

    def start_capture(self):
        # For QuickTime, you might need to set the correct video device index or path
        cap = cv2.VideoCapture(self.source)
        if not cap.isOpened():
            raise IOError("Cannot open video source")
        return cap
