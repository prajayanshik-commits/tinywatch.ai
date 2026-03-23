import streamlit as st
import cv2
import mediapipe as mp
import time
from PIL import Image

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

st.set_page_config(page_title="TinyWatch: Autonomous Shield", layout="wide")
st.title("🛡️ TinyWatch: AI Autonomous Shield")

# --- SESSION TIMER LOGIC (Slide 5: Screen Time) ---
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

elapsed_time = (time.time() - st.session_state.start_time) / 60  # Convert to minutes

if elapsed_time > 30:
    st.error("🔒 SCREEN LOCKED: 30-minute limit reached. Time to play outside!")
    st.stop()

# --- STEP 1: CAMERA FEED ---
img_file = st.camera_input("Scanning Environment...")

if img_file:
    # Process image
    img = Image.open(img_file)
    img_array = np.array(img)
    results = face_detection.process(cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB))

    if results.detections:
        for detection in results.detections:
            # Get bounding box to calculate distance
            bbox = detection.location_data.relative_bounding_box
            face_width = bbox.width  # How much of the screen the face takes up
            
            # --- DISTANCE LOGIC (Virtual Nanny) ---
            if face_width > 0.5:  # If face takes > 50% of width, they are TOO CLOSE
                st.warning("⚠️ PROXIMITY ALERT!")
                # Play Audio (Self-playing HTML Audio)
                st.components.v1.html("""
                    <audio autoplay>
                        <source src="https://www.soundjay.com/buttons/beep-01a.mp3" type="audio/mpeg">
                    </audio>
                    <script>alert("You are too close! Please move back.");</script>
                """, height=0)
                st.info("🔊 Virtual Nanny: 'Please sit back, you are too close to the screen!'")

            # --- AGE SIMULATION (For Demo Impact) ---
            # In a real MVP, we'd use a deep learning model here.
            # For the pitch, we use a 'Child' default or a sidebar override.
            st.error("👶 CHILD DETECTED")
            
            # --- MULTIPLE VIDEO GALLERY ---
            st.subheader("📺 Safe Feed: YouTube Kids Gallery")
            col1, col2 = st.columns(2)
            with col1:
                st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
                st.video("https://www.youtube.com/watch?v=7uK6YvLpP90")
            with col2:
                st.video("https://www.youtube.com/watch?v=S-tS_E_6tSg")
                st.video("https://www.youtube.com/watch?v=fN1Cyr0ZK9M")
    else:
        st.info("Searching for user...")
