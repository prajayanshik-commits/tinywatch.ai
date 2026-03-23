import streamlit as st
import cv2
import time
import pyttsx3

st.title("Smart Screen AI MVP")

# Voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

run = st.button("Start Camera")

FRAME_WINDOW = st.image([])

start_time = time.time()
warning_spoken = False

if run:
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            st.write("Camera Error")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        content_text = "No face detected"

        for (x, y, w, h) in faces:

            # Dummy age detection
            if w < 120:
                age = 10
                content_text = "👶 Kids Content"
                youtube_link = "https://www.youtube.com/kids"
            else:
                age = 20
                content_text = "🧑 Adult Content"
                youtube_link = "https://www.youtube.com"

            # Distance warning
            if w > 200 and not warning_spoken:
                speak("You are too close to the screen")
                warning_spoken = True

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, f"Age: {age}", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        # Show content type
        st.write(content_text)

        if "youtube_link" in locals():
            st.markdown(f"[Open Content]({youtube_link})")

        FRAME_WINDOW.image(frame, channels="BGR")

        # Timer (30 min)
        if time.time() - start_time > 1800:
            speak("30 minutes over. Screen will close.")
            st.warning("⏱️ Time Over")
            break

    cap.release()
