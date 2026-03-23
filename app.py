import streamlit as st
import cv2
import numpy as np
import time

st.set_page_config(page_title="TinyWatch: Smart Scan", layout="wide")
st.title("🛡️ TinyWatch: Automatic AI Protector")

# --- THE AUTO-SCANNER ---
img_file = st.camera_input("Scanning Face...", label_visibility="hidden")

if img_file:
    # Convert image for analysis
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    height, width, _ = img.shape
    
    # Initialize OpenCV Face Detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # Calculate face size relative to screen
            face_area = (w * h) / (width * height)
            
            # --- THE AUTOMATIC LOGIC ---
            # If face_area is large, we assume it's a child close to the screen
            if face_area > 0.18: 
                # ✅ CHILD DETECTED (GREEN)
                st.markdown("<h2 style='color: #28a745; text-align: center;'>✅ CHILD DETECTED</h2>", unsafe_allow_html=True)
                
                # SPEAKER: Only shows if they are 'Child' and 'Too Close'
                st.markdown("""
                    <div style="background-color: #ffcccc; padding: 20px; border-radius: 10px; border: 3px solid red;">
                        <h2 style='color: red; text-align: center; margin: 0;'>🔊 SPEAKER: 'Please sit back, be far from the screen!'</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.write("---")
                st.subheader("📺 Safe Kids Feed")
                col1, col2 = st.columns(2)
                with col1: st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
                with col2: st.video("https://www.youtube.com/watch?v=71h8MZshGSs")
            
            else:
                # 👤 ADULT DETECTED (BLUE)
                st.markdown("<h2 style='color: #007bff; text-align: center;'>👤 ADULT DETECTED</h2>", unsafe_allow_html=True)
                st.success("Adult access granted. Safe distance verified.")
                st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Standard Video
    else:
        st.warning("🔍 No face detected. Please stand in front of the camera.")

# 30 Minute Lock Logic
if 'start' not in st.session_state: st.session_state.start = time.time()
if (time.time() - st.session_state.start) / 60 >= 30:
    st.error("🔒 SCREEN LOCKED: 30-Minute Limit Reached.")
    st.stop()
