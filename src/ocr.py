import pytesseract
import cv2

class OCR:
    def __init__(self, tesseract_cmd):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def extract_text(self, image):
        # Convert image to grayscale and apply thresholding if needed
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Optional: apply additional preprocessing like thresholding
        text = pytesseract.image_to_string(gray, config="--psm 8")
        return text.strip()
