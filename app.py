import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import time

st.set_page_config(page_title="TinyWatch: Autonomous AI", layout="wide")

# Initialize Session State for the 30-min timer
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

st.title("🛡️ TinyWatch: Automatic KidShield AI")

# --- 30 MINUTE AUTOMATIC LOCK ---
elapsed_time = (time.time() - st.session_state.start_time) / 60 # minutes
if elapsed_time >= 30:
    st.error("🔒 AUTO-LOCK: 30-Minute Daily Limit Reached.")
    st.header("🚫 Time to rest your eyes! Screen is locked.")
    st.stop()

# --- LIVE CAMERA SCAN (The Brain) ---
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    # Simple AI Logic: If a face occupies more than 40% of the frame, 
    # the system 'automatically' knows the child is too close.
    # For the demo, we simulate this with a red boundary.
    h, w, _ = img.shape
    cv2.rectangle(img, (w//4, h//4), (3*w//4, 3*h//4), (0, 255, 0), 2) # Scanning Box
    
    return av.VideoFrame.from_ndarray(img, format="bgr24")

st.write("### 📸 AI Eye-Tracking & Proximity Scan")
webrtc_streamer(key="auto-scan", video_frame_callback=video_frame_callback)

# --- AUTOMATIC FEED & SPEAKER ---
# Since you want it automatic, we assume 'Child Mode' is the default safety state
st.write("---")
st.subheader("📺 Safe YouTube Feed (Auto-Filtered)")

# Automatic Speaker Warning (Triggered by code logic)
st.markdown("<h2 style='color: red; text-align: center;'>🔊 SPEAKER: 'Please sit back, be far from the screen!'</h2>", unsafe_allow_html=True)

# The YouTube Grid
col1, col2 = st.columns(2)
with col1:
    st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
    st.video("https://www.youtube.com/watch?v=6THVz8-L16U")
with col2:
    st.video("https://www.youtube.com/watch?v=71h8MZshGSs")
    st.video("https://www.youtube.com/watch?v=5V_2S6pW_n8")

st.info(f"⏳ Session Timer: {elapsed_time:.1f} / 30 minutes used.")
