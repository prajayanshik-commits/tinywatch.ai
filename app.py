import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.set_page_config(page_title="TinyWatch: Auto-Scan", layout="wide")
st.title("🛡️ TinyWatch: Automatic KidShield AI")

# --- AUTO-SCANNING LOGIC ---
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    h, w, _ = img.shape
    
    # We use a simple visual box to represent the 'Safe Zone'
    # In a full model, this is where the CNN Age Detection runs
    cv2.rectangle(img, (w//4, h//4), (3*w//4, 3*h//4), (0, 255, 0), 2)
    
    return av.VideoFrame.from_ndarray(img, format="bgr24")

st.write("### 📸 AI Eye-Tracking & Proximity Scan")
st.info("💡 Click 'START' below to begin autonomous monitoring.")

# The Camera Component
webrtc_streamer(key="auto-scan", video_frame_callback=video_frame_callback)

# --- THE "NANNY" SPEAKER & FEED ---
st.write("---")

# Visual Warning for the Demo
st.markdown("<h2 style='color: red; text-align: center; border: 5px solid red; padding: 10px;'>🔊 SPEAKER: 'Please sit back, be far from the screen!'</h2>", unsafe_allow_html=True)

st.subheader("📺 Safe YouTube Feed (Auto-Filtered for Kids)")

# 4-Video Grid as requested
col1, col2 = st.columns(2)
with col1:
    st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
    st.video("https://www.youtube.com/watch?v=6THVz8-L16U")
with col2:
    st.video("https://www.youtube.com/watch?v=71h8MZshGSs")
    st.video("https://www.youtube.com/watch?v=5V_2S6pW_n8")
