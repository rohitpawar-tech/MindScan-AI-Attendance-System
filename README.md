# mindscan-ai-flask-attendance-webapp
mindscan-ai-flask-attendance-webapp

# MindScan AI — Flask Attendance Web App

MindScan AI is a Flask-based web application for automated student attendance.  
It uses **real-time eye detection** and simulated **mask detection** to ensure accurate attendance logging in a CSV file.

---

## Features

- Web interface for entering student ID  
- Real-time eye detection using OpenCV  
- Simulated mask detection  
- Attendance logged with date and time  
- Prevents duplicate entries for the same student on the same day  
- Randomized confirmation messages for users  

---

## Tech Stack

- Python 3  
- Flask  
- OpenCV  
- HTML / CSS / JavaScript  
- CSV for attendance storage  

---

## How It Works

1. Student enters ID on the web form  
2. Webcam activates to detect eyes  
3. Mask detection is simulated  
4. Attendance is logged in `attendance.csv`  
5. Duplicate entries are prevented  
6. User receives a confirmation message  

---

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/mindscan-ai-flask-attendance-webapp.git

# MindScan AI — Flask Attendance Web App

MindScan AI is a Flask-based web application for automated student attendance.  
It uses **real-time eye detection** and simulated **mask detection** to ensure accurate attendance logging in a CSV file.

---

## Features

- Web interface for entering student ID  
- Real-time eye detection using OpenCV  
- Simulated mask detection  
- Attendance logged with date and time  
- Prevents duplicate entries for the same student on the same day  
- Randomized confirmation messages for users  

---

## Tech Stack

- Python 3  
- Flask  
- OpenCV  
- HTML / CSS / JavaScript  
- CSV for attendance storage  

---

## How It Works

1. Student enters ID on the web form  
2. Webcam activates to detect eyes  
3. Mask detection is simulated  
4. Attendance is logged in `attendance.csv`  
5. Duplicate entries are prevented  
6. User receives a confirmation message  

---

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/mindscan-ai-flask-attendance-webapp.git

pip install flask opencv-python

python app.py

http://127.0.0.1:5000/

folder structure:
mindscan-ai-flask-attendance-webapp/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
├── attendance.csv
└── README.md

Future Improvements:

-Integrate real mask detection ML model

-Add face recognition for accurate attendance

-Use a database (MySQL/MongoDB) instead of CSV

-Admin dashboard for summary and analytics

-Export attendance reports to Excel or PDF
