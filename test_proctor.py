import cv2

from modules.proctor_detector import (
    ProctorDetector
)

detector = ProctorDetector()

cap = cv2.VideoCapture(0)

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

    # Run YOLO every 30 frames
    if frame_count % 30 == 0:

        frame = detector.detect(
            frame
        )

    cv2.imshow(
        "AI Proctoring",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()