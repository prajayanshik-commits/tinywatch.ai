import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

st.set_page_config(page_title="TinyWatch: Auto-Scan", layout="wide")

# Sidebar - Matching your screenshot
st.sidebar.title("👤 Demo Controller")
app_mode = st.sidebar.radio("AI Detection Result:", ["Child (Age 7)", "Adult (Age 25)"])
proximity_slider = st.sidebar.slider("Proximity Sensor (cm):", 0, 100, 46)

st.title("🛡️ TinyWatch AI: Real-Time Shield")

# Function to process video frames automatically
def callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    # Logic: If 'Child' and 'Slider' is low, show alert on video
    if app_mode == "Child (Age 7)" and proximity_slider < 30:
        cv2.putText(img, "WARNING: TOO CLOSE!", (50, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
    
    return av.VideoFrame.from_ndarray(img, format="bgr24")

# The Live Video Component
webrtc_streamer(key="tinywatch-scan", video_frame_callback=callback)

if app_mode == "Child (Age 7)":
    if proximity_slider < 30:
        st.error("🚨 SPEAKER: 'Please sit back, you are too close!'")
    st.subheader("📺 Safe Kids Feed")
    col1, col2 = st.columns(2)
    with col1: st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
    with col2: st.video("https://www.youtube.com/watch?v=71h8MZshGSs")
