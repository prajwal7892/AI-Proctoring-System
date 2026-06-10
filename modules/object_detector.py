from ultralytics import YOLO
import cv2


class ObjectDetector:

    def __init__(self):

        print("Loading YOLO model...")

        self.model = YOLO("yolov8n.pt")

        self.target_classes = {
            0: "Person",
            67: "Cell Phone",
            73: "Book"
        }

    def detect(self, frame):

        results = self.model(
            frame,
            verbose=False,
            imgsz=320,
            conf=0.5
        )

        detections = []

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                if cls not in self.target_classes:
                    continue

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                conf = float(box.conf[0])

                label = self.target_classes[cls]

                detections.append(label)

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"{label} {conf:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

        return frame, detections