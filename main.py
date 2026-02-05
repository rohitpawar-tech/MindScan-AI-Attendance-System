from flask import Flask, render_template, request
import os
import cv2
import random
from datetime import datetime

app = Flask(__name__)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# ---- Complete Student Database ----
students = {
    "240105041001": "BHALERAO SIDDHARTH ARUN",
    "240105131129": "PATIL UTKARSH SHANKAR",
    "240105231023": "KHANDBAHALE SAKSHI SHARAD",
    "240105311001": "PANDIT MANISHA DILIP",
    "240105311002": "BOTHE VEDANT PRAKASH",
    "240105311004": "SHAIKH REHAN IMRAN",
    "240105311005": "CHAUDHARI HRUSHIKESH MANOJ",
    "240105311006": "PAWAR ROHIT SANDIP",
    "240105311007": "YADAV RUDRAKSH LALIT",
    "240105311008": "GAIKWAD SAKSHAM YOGESH",
    "240105311009": "BODKE ADITYA SANJAY",
    "240105311010": "ICHAKE PRITAL KAILAS",
    "240105311011": "DESHMUKH TANISH SHIVAJI",
    "240105311012": "PAWAR SHRAVANI SANDEEP",
    "240105311013": "KHUSHALI ASHOK KHAIRNAR",
    "240105311015": "PANDEY KHUSHI SHRILAL",
    "240105311016": "SAYYED REHAN LATIF",
    "240105311018": "SHAIKH MOHAMMAD SAALIM AQUEEL",
    "240105311019": "TIWARI RAHUL TRIBHUVANNATH",
    "240105311020": "SHAIKH MUJAHID SHAIKH AKBAR",
    "240105311021": "SHAIKH ARSALAN ASHPAK",
    "240105311022": "BUNGE SAURBH NIMBA",
    "240105311023": "AHER TANUJA SANDIP",
    "240105311024": "MENDA ANKITA PURUSHOTHAM",
    "240105311025": "ADKINE BHAGWAN VIJAY",
    "240105311027": "PANDEY SNEHA ANIL",
    "240105311028": "SHEKH REHAN ANWAR",
    "240105311029": "TUVAR YASHPAL BHURESING",
    "240105311030": "CHAVAN HARSHAL RAJENDRA",
    "240105311031": "SONAWANE PRIYANKA KUNDAN",
    "240105311032": "VIDHATE AMOL ANIL",
    "240105311033": "MANDLIK AJINKYA DATTU",
    "240105311034": "GAWALI RIYA SHEKHAR",
    "240105311036": "MUSADDI HUSSAIN MUSTAFA",
    "240105311037": "RAJPUT SRUJAL BHANUPRATAPSING",
    "240105311038": "AMBUSKR RUSHIKESH GAJANAN",
    "240105311039": "PAWAR VAIBHAV VILAS",
    "240105311042": "PATHAN AFTAB SAJID",
    "240105311043": "CHOUDHARY DURGA PUKHRAJ",
    "240105311044": "KHARAT YASH BHAGWAT",
    "240105311045": "KHADE KARTIK KISHOR",
    "240105311046": "BADAKH SUYASH APPASAHEB",
    "240105311047": "WAGH MOHIT MANISH",
    "240105311048": "TAMBOLI AMAAN WASEEM",
    "240105311049": "TAMBOLI AYAN WASEEM",
    "240105311050": "AVHALE PRATIKSHA MINANATH",
    "240105311051": "JADHAV SARTHAK SUNIL",
    "240105311052": "JADHAV ROHAN RAJENDRA",
    "240105311053": "VAMAJA DRASHTI PARESHBHAI",
    "240105311054": "SURYAWANSHI TEJAS DHANRAJ",
    "240105311055": "VARADE PRIYA SANJAY",
    "240105311056": "PAWAR JAYESH RAMCHANDRA",
    "240105311057": "TIDME KARTIK NITIN",
    "240105311058": "SINGH ARYAN RAKESH",
    "240105311059": "ANSARI ARIFNAWAJ NURHASAN",
    "240105311061": "BHOR MAYUR BALU",
    "240105311063": "YADAV TANVI PRASHANT",
    "240105311064": "KALE SHRUSHTI NILESH",
    "240105311065": "SHAIKH KASHAF MASOOD",
    "240105311066": "NIKAM SHIVARAJ BHASKAR",
    "240105311067": "JAWARE VYANKATESH VIVEKANAND",
    "240105311068": "BHARTI SHIVANSHU SHIVKUMAR",
    "240105311069": "SAVALE NIKHIL MADHUKAR",
    "240105311071": "BOCHARE BABAN GANESH",
    "240105311072": "SHIRSATH TEJAS KIRAN",
    "240105311073": "SALUNKE RUSHIKESH UMAKANT",
    "240105311074": "MAHAJAN SARTHAK MAHENDRA",
    "240105311075": "SAUD SHAKUNTALA CHANDARBHADUR",
    "240105311076": "SHINDE DARSHANA DIGAMBAR",
    "240105311077": "RATHOD ABHIJIT RAMRAO",
    "240105311078": "DESHMANE CHETAN SANTOSH",
    "240105311079": "AASHIQ ILAHI MOHIBBUR RAHAMAN",
    "240105311080": "SAVANT ANJALI SANDIP",
    "240105311081": "KEDAR NIKHIL JAGANNATH",
    "240105311082": "KAKAD ASHUTOSH RATAN",
    "240105311083": "KANADE CHAITANYA GANESH",
    "240105311084": "NANAWRE SIDDHANT VINAYAK",
    "240105341001": "BHADANE KARTIK RAJENDRA",
    "240105341002": "SHUKLA SOHAM ANIRUDDHA",
    "240105341004": "SINGH GARIMA SANDEEP",
    "240105341005": "BANKAR AAKASH RAJENDRA",
    "240105341006": "SARAF RAJ DILIP",
    "240105341007": "SINGH KUNAL SANJAY",
    "240105341008": "BAGUL HARSH RAVINDRA",
    "240105341009": "PURI GANGADHAR AVDHOOT",
    "240105341010": "KATARE PRATIK BALU",
    "240105341011": "PASHA GULAM HUSAIN",
    "240105341012": "SONAR MAYUR UMESH",
    "240105341013": "QURESHI ARKAN ANWAR",
    "240105341014": "RAJE SAHIL SANDEEP",
    "240105341015": "GOSAVI RUSHIKESH KRUSHNAGIRI",
    "240105341016": "SABLE TANMAY SANTOSH",
    "240105341018": "KUMBHAR KUNAL BHARAT",
    "240105341020": "RAJOLE GAURAV RAMDAS",
    "240105341024": "DATIR RUSHIKESH SATISH",
    "240105341026": "BORSE MAHESH BHARAT",
    "240105341028": "MUNDHE ADITYA DATTATRAY",
    "240105341032": "KSHIRSAGAR ISHWAR GORAKH",
    "240105341033": "KSHIRSAGAR VEDSHREE CHANDRAKANT",
    "240105341034": "JADHAV VAISHNAVI YOGESH",
    "240105341036": "NIKAM CHETAN SUNIL"
}

# ---- Eye Detection from Webcam ----
def detect_eyes_from_camera():
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
    cap = cv2.VideoCapture(0)
    detected = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Eye Detection - Press Q to Capture", frame)

        if len(eyes) > 0:
            detected = True

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return detected

# ---- Dummy Mask Detection ----
def detect_mask():
    return random.choice(["Mask", "No Mask"])

# ---- Attendance Logger ----
def mark_attendance(student_id, status):
    file_path = os.path.join(PROJECT_ROOT, "attendance.csv")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Prevent duplicate attendance for the same student today
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if student_id in line and line.split(",")[3].startswith(datetime.now().strftime("%Y-%m-%d")):
                    return False  # Already marked today

    with open(file_path, "a") as f:
        name = students.get(student_id, "Unknown Student")
        f.write(f"{student_id},{name},{status},{now}\n")
    return True

# ---- Routes ----
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance_api():
    student_id = request.form['student_id']

    if student_id not in students:
        return {"status": "error", "message": "❌ Student not found!"}, 404

    # Mark attendance only if eyes detected
    if detect_eyes_from_camera():
        mask_status = detect_mask()
        status = "Present (Mask)" if mask_status == "Mask" else "Absent (No Mask)"
    else:
        status = "Absent (No Eyes Detected)"

    if not mark_attendance(student_id, status):
        return {"status": "error", "message": "❌ Attendance already marked today!"}, 400

    success_messages = [
        "✅ Attendance marked successfully!",
        "🎉 Great! You are logged in.",
        "📝 Attendance recorded!",
        "👏 Done! Have a nice day."
    ]
    random_message = random.choice(success_messages)

    return {
        "status": "success",
        "message": random_message,
        "student": students[student_id],
        "attendance_status": status
    }

if __name__ == '__main__':
    app.run(debug=True)
