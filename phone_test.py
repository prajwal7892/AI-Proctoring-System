# phone_test.py

from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(
        frame,
        imgsz=320,
        verbose=False
    )

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            if cls in [0, 67, 73]:

                print(
                    result.names[cls]
                )

    cv2.imshow(
        "Phone Test",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()