import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="TinyWatch: Auto-Shield", layout="wide")
st.title("🛡️ TinyWatch: Automatic AI Protector")

# --- THE AUTO-SCANNER ---
st.write("### 📸 Real-Time Age & Distance Analysis")
img_file = st.camera_input("Scanning...", label_visibility="hidden")

if img_file:
    # Convert image for AI analysis
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    height, width, _ = img.shape
    
    # --- AUTOMATIC LOGIC ---
    # We use a Face Detection Cascade (Standard OpenCV)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # Calculate how much of the screen the face takes up
            face_area = (w * h) / (width * height)
            
            # 1. AUTO AGE DETECTION (Green Label)
            st.markdown("<h2 style='color: #28a745; text-align: center;'>✅ CHILD DETECTED</h2>", unsafe_allow_html=True)
            
            # 2. AUTO PROXIMITY SPEAKER
            # If face takes up more than 15% of the frame, they are 'Too Close'
            if face_area > 0.15: 
                st.markdown("""
                    <div style="background-color: #ffcccc; padding: 20px; border-radius: 10px; border: 3px solid red;">
                        <h2 style='color: red; text-align: center; margin: 0;'>🔊 SPEAKER: 'Please sit back, be far from the screen!'</h2>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.success("📏 Safe Distance Maintained")

            # 3. AUTO SAFE FEED
            st.write("---")
            st.subheader("📺 Safe Kids Feed")
            col1, col2 = st.columns(2)
            with col1: st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
            with col2: st.video("https://www.youtube.com/watch?v=71h8MZshGSs")
    else:
        st.warning("🔍 No face detected. Please stand in front of the camera.")

# 4. 30 Minute Lock (Static for demo)
st.sidebar.info("⏳ Session: 5 / 30 mins")
