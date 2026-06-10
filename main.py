import cv2
from modules.head_pose import HeadPoseDetector

detector = HeadPoseDetector()

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        print("Could not access webcam")
        break

    frame, status = detector.process(frame)

    cv2.imshow(
        "AI Proctoring System",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()