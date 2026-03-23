import streamlit as st
import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe for Real-time tracking
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

st.set_page_config(page_title="TinyWatch: Zero-UI Shield", layout="wide")

# Sidebar - Matching your screenshot (efg.jpeg)
st.sidebar.title("👤 Demo Controller")
app_mode = st.sidebar.radio("AI Detection Result:", ["Child (Age 7)", "Adult (Age 25)"])
proximity_slider = st.sidebar.slider("Proximity Sensor (cm):", 0, 100, 46)

st.title("🛡️ TinyWatch AI: Automatic Protection")

# The "Direct Scan" placeholder
FRAME_WINDOW = st.image([]) 
camera = cv2.VideoCapture(0) # Starts the webcam automatically

while True:
    ret, frame = camera.read()
    if not ret:
        break
    
    # Convert for processing
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)
    
    # Check for proximity automatically
    if proximity_slider < 30 and app_mode == "Child (Age 7)":
        cv2.putText(frame, "⚠️ TOO CLOSE! SIT BACK", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        st.warning("🚨 SPEAKER ALERT: 'Please sit back, protect your eyes!'")
    
    # Show the live scan to the judges
    FRAME_WINDOW.image(frame_rgb)

    # Content Logic
    if app_mode == "Child (Age 7)":
        st.subheader("📺 Safe Kids Feed Activated")
        # Grid of videos would go here
    else:
        st.subheader("📺 Adult Access Granted")
