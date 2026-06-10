from cvzone.FaceMeshModule import FaceMeshDetector
from modules.alert_logger import AlertLogger

import cv2
import time
import os


class HeadPoseDetector:

    def __init__(self):

        self.detector = FaceMeshDetector(maxFaces=1)

        self.violation_count = 0
        self.start_time = None
        self.alert_triggered = False

        self.alert_folder = "alerts"
        os.makedirs(self.alert_folder, exist_ok=True)

        self.logger = AlertLogger()

    def process(self, frame):

        frame, faces = self.detector.findFaceMesh(
            frame,
            draw=True
        )

        status = "No Face"

        if faces:

            face = faces[0]

            nose = face[1]

            cv2.circle(
                frame,
                nose,
                5,
                (0, 255, 0),
                cv2.FILLED
            )

            h, w, _ = frame.shape
            center_x = w // 2

            if nose[0] < center_x - 100:
                status = "Looking Left"

            elif nose[0] > center_x + 100:
                status = "Looking Right"

            else:
                status = "Looking Center"

            # -------------------------
            # Violation Logic
            # -------------------------

            if status != "Looking Center":

                if self.start_time is None:
                    self.start_time = time.time()

                elapsed = time.time() - self.start_time

                if elapsed > 2 and not self.alert_triggered:

                    self.violation_count += 1
                    self.alert_triggered = True

                    filename = os.path.join(
                        self.alert_folder,
                        f"violation_{self.violation_count}.jpg"
                    )

                    cv2.imwrite(
                        filename,
                        frame
                    )

                    print(
                        f"[ALERT SAVED] {filename}"
                    )

                    self.logger.log_alert(
                        "Head Pose Violation",
                        filename
                    )

            else:
                self.start_time = None
                self.alert_triggered = False

            cv2.putText(
                frame,
                status,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Violations: {self.violation_count}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

        return frame, status