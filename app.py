import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="TinyWatch: AI Shield", layout="wide")
st.title("🛡️ TinyWatch: Autonomous AI Shield")

# --- AUTO-DETECTION ENGINE ---
# This replaces the "buttons" with actual logic
def detect_user_and_distance(image):
    # Convert image to OpenCV format
    img = np.array(image.convert('RGB'))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Load the pre-trained Face Detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            # DISTANCE MATH: Smaller 'w' (width) means person is far. Larger means close.
            # In a real app, we use 500 / w to estimate cm.
            approx_dist = 5000 / w 
            
            # AGE MATH: Simple simulation based on face height for the demo
            # A child's face structure is smaller relative to the frame
            is_child = True if h < 180 else False 
            
            return is_child, approx_dist
    return None, None

# --- UI START ---
img_file = st.camera_input("Scanning Face...")

if img_file:
    # 1. Open the image
    input_img = Image.open(img_file)
    
    # 2. RUN AUTO-DETECTION
    is_child, distance = detect_user_and_distance(input_img)
    
    if is_child is not None:
        if is_child:
            st.error(f"🚫 CHILD DETECTED | Approx Distance: {int(distance)}cm")
            
            # SAFETY LOGIC
            if distance < 40:
                st.warning("🔊 SPEAKER: 'SIT BACK! YOU ARE TOO CLOSE!'")
                st.error("🔒 SCREEN LOCKED FOR EYE SAFETY")
            else:
                st.subheader("📺 YouTube Kids Active")
                st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
        else:
            st.success(f"✅ ADULT DETECTED | Approx Distance: {int(distance)}cm")
            st.subheader("📺 Standard YouTube Feed")
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        st.info("No face detected. Please center yourself in the camera.")
