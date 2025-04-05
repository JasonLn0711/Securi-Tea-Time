import cv2
import numpy as np

def reidentify_person(frame, bbox):
    # Crop the person's region from the frame
    x, y, w, h = bbox
    person_img = frame[y:y+h, x:x+w]
    
    # Calculate a color histogram as a simple re-identification feature
    hsv = cv2.cvtColor(person_img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [50, 60], [0, 180, 0, 256])
    cv2.normalize(hist, hist)
    # For now, simply return the flattened histogram as an ID
    # In a real system, you might compare this against a database of known histograms.
    person_id = np.array2string(hist.flatten(), precision=2, separator=',')
    return person_id
