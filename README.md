# AI-Proctoring-System
# AI Proctoring System

## Overview

AI Proctoring System is a computer vision-based online examination monitoring system developed using Python, OpenCV, YOLOv8, SQLite, and Streamlit.

The system monitors candidate behavior during online examinations and detects suspicious activities such as:

* Looking away from the screen
* Mobile phone usage
* Book usage
* Multiple persons in front of the camera

All violations are logged into a SQLite database, screenshots are captured automatically, and PDF reports can be generated for review.

---

## Features

* Head Movement Monitoring
* Violation Detection and Counting
* Screenshot Capture
* SQLite Database Logging
* Mobile Phone Detection using YOLOv8
* Book Detection using YOLOv8
* Multiple Person Detection
* PDF Report Generation
* Streamlit Dashboard

---

## Technology Stack

* Python 3.11
* OpenCV
* CVZone
* YOLOv8 (Ultralytics)
* SQLite
* Streamlit
* FPDF2

---

## Project Structure

AI_Proctoring/

├── modules/

│ ├── alert_logger.py

│ ├── head_pose.py

│ ├── object_detector.py

│ ├── proctor_detector.py

│ └── report_gen.py

├── alerts/

├── reports/

├── main.py

├── app.py

├── generate_report.py

├── test_proctor.py

├── alerts.db

└── README.md

---

## Installation

### Clone Repository

git clone https://github.com/prajwal7892/AI-Proctoring-System.git

cd AI-Proctoring-System

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install opencv-python

pip install cvzone

pip install ultralytics

pip install streamlit

pip install pandas

pip install fpdf2

pip install numpy

---

## Running the Project

### Head Pose Monitoring

python main.py

### YOLO Proctoring Detection

python test_proctor.py

### Generate PDF Report

python generate_report.py

### Launch Dashboard

streamlit run app.py --server.port 9999

Open:

http://localhost:9999

---

## Database

The system uses SQLite.

Violation logs are stored in:

alerts.db

Each record contains:

* Timestamp
* Alert Type
* Screenshot Path

---

## Future Enhancements

* Eye Gaze Tracking
* Face Recognition
* Email Alerts
* Cloud Deployment
* Real-Time Streamlit Monitoring

---

## Author

M Prajwal

Master of Computer Applications (MCA)

NHCE, Bengaluru
