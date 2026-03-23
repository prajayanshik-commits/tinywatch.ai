import cv2
import pyttsx3
import time
import numpy as np

# Text to speech engine
engine = pyttsx3.init()

# Start time
start_time = time.time()

# Load face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Dummy age prediction function (replace with real AI model later)
def predict_age(face_img):
    h, w = face_img.shape[:2]
    if w < 100:
        return 10   # assume kid
    else:
        return 20   # assume adult

# Distance estimation (based on face size)
def estimate_distance(face_width):
    if face_width > 200:
        return "too close"
    else:
        return "safe"

# Camera start
cap = cv2.VideoCapture(0)

warning_spoken = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]

        age = predict_age(face_img)

        # Age-based content
        if age < 15:
            content = "Showing Kids Content"
            youtube_link = "https://www.youtube.com/kids"
        else:
            content = "Showing Adult Content"
            youtube_link = "https://www.youtube.com"

        # Distance check
        distance = estimate_distance(w)

        if distance == "too close" and not warning_spoken:
            engine.say("You are too close to the screen")
            engine.runAndWait()
            warning_spoken = True

        # Display info
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f"Age: {age}", (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        cv2.putText(frame, content, (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

    # Show frame
    cv2.imshow("Smart MVP System", frame)

    # 30 minutes timer
    elapsed_time = time.time() - start_time
    if elapsed_time > 1800:  # 1800 sec = 30 min
        engine.say("Screen time is over. Shutting down.")
        engine.runAndWait()
        break

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
