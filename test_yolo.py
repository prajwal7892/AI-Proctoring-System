import cv2
from modules.object_detector import ObjectDetector

detector = ObjectDetector()

cap = cv2.VideoCapture(0)

frame_count = 0
detections = []

while True:

    success, frame = cap.read()

    if not success:
        break

    frame_count += 1

    # Resize frame for speed
    frame = cv2.resize(frame, (640, 480))

    # Run YOLO every 30 frames
    if frame_count % 30 == 0:
        frame, detections = detector.detect(frame)

    cv2.putText(
        frame,
        f"Detections: {', '.join(detections)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    cv2.imshow("YOLO Test", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()