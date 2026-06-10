from ultralytics import YOLO
from modules.alert_logger import AlertLogger

import cv2
import os
import time


class ProctorDetector:

    def __init__(self):

        self.model = YOLO("yolov8n.pt")

        self.logger = AlertLogger()

        self.alert_folder = "alerts"
        os.makedirs(
            self.alert_folder,
            exist_ok=True
        )

        self.last_alert_time = {}

        self.target_classes = {
            0: "Person",
            67: "Cell Phone",
            73: "Book"
        }

    def detect(self, frame):

        results = self.model(
            frame,
            imgsz=320,
            verbose=False
        )

        person_count = 0

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                if cls not in self.target_classes:
                    continue

                label = self.target_classes[cls]

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

                if label == "Person":
                    person_count += 1

                if label in ["Cell Phone", "Book"]:

                    self.save_alert(
                        frame,
                        f"{label} Detected"
                    )

        if person_count > 1:

            self.save_alert(
                frame,
                "Multiple Persons Detected"
            )

        return frame

    def save_alert(
        self,
        frame,
        alert_type
    ):

        current_time = time.time()

        if alert_type in self.last_alert_time:

            if (
                current_time
                - self.last_alert_time[alert_type]
            ) < 5:
                return

        self.last_alert_time[
            alert_type
        ] = current_time

        timestamp = int(current_time)

        filename = os.path.join(
            self.alert_folder,
            f"{alert_type}_{timestamp}.jpg"
        )

        cv2.imwrite(
            filename,
            frame
        )

        self.logger.log_alert(
            alert_type,
            filename
        )

        print(
            f"[YOLO ALERT] {alert_type}"
        )