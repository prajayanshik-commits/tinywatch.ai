import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import time

st.set_page_config(page_title="TinyWatch: Autonomous Shield", layout="wide")

# --- SIDEBAR (Demo Controller) ---
st.sidebar.title("👤 Demo Controller")
app_mode = st.sidebar.radio("User Identity:", ["Child (Age 7)", "Adult (Age 25)"])
proximity = st.sidebar.slider("Proximity (cm):", 0, 100, 45)
session_time = st.sidebar.slider("Session Time (Minutes):", 0, 40, 5)

st.title("🛡️ TinyWatch AI: Automatic Protection")

# --- 30 MINUTE LOCK LOGIC ---
if session_time >= 30:
    st.error("🔒 SCREEN LOCKED: 30-Minute Limit Reached!")
    st.header("🚫 Time for a break! Go play outside.")
    st.stop() # This stops the app from showing anything else

# --- LIVE CAMERA FEED (Auto-Scan) ---
def video_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    # Draw the 'Distance Line' if too close
    if proximity < 30 and app_mode == "Child (Age 7)":
        # Red Border/Line on the video itself
        cv2.rectangle(img, (10, 10), (img.shape[1]-10, img.shape[0]-10), (0, 0, 255), 10)
        cv2.putText(img, "!!! TOO CLOSE !!!", (100, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    
    return av.VideoFrame.from_ndarray(img, format="bgr24")

st.write("### 📸 Live AI Monitoring")
webrtc_streamer(key="tinywatch-scan", video_frame_callback=video_callback)

# --- THE NANNY / SPEAKER LOGIC ---
if app_mode == "Child (Age 7)":
    if proximity < 30:
        st.markdown("<h1 style='text-align: center; color: red;'>🔊 SPEAKER: 'Please sit back, you are too close!'</h1>", unsafe_allow_html=True)
        st.warning("⚠️ **VIRTUAL NANNY:** Distance Alert Active. Please move away from the screen.")
    
    st.write("---")
    st.subheader("📺 Safe Kids Feed (YouTube Kids API)")
    
    # 4-Video Grid
    col1, col2 = st.columns(2)
    with col1: st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
    with col2: st.video("https://www.youtube.com/watch?v=71h8MZshGSs")
    
    col3, col4 = st.columns(2)
    with col3: st.video("https://www.youtube.com/watch?v=6THVz8-L16U")
    with col4: st.video("https://www.youtube.com/watch?v=5V_2S6pW_n8")

else:
    st.success("✅ Adult Detected - Full Access")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
