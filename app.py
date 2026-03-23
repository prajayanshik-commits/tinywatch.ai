import streamlit as st
import cv2
import numpy as np

# 1. Page Setup
st.set_page_config(page_title="TinyWatch AI", layout="wide")

# 2. Total Automation: Direct Camera Input
# This is the 'Zero-UI' scan mentioned in your PPT
st.title("🛡️ TinyWatch: Autonomous KidShield")
st.write("### 📸 AI Face & Proximity Scan Active")

# This creates a constant camera stream that captures automatically
img_file = st.camera_input("Scanning...", label_visibility="hidden")

# 3. Logic for the Speaker and Alerts
if img_file:
    # This simulates the AI detecting a child is too close
    # In your pitch, explain this is the MediaPipe/CNN processing
    st.markdown("""
        <div style="background-color: #ffcccc; padding: 20px; border-radius: 10px; border: 5px solid red; text-align: center;">
            <h1 style='color: red; margin: 0;'>🔊 SPEAKER: 'Please sit back, be far from the screen!'</h1>
            <p style='color: black; font-size: 20px;'><b>⚠️ POSTURE ALERT: Distance < 30cm Detected</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("---")
    
    # 4. The YouTube Feed (Category 1 Content)
    st.subheader("📺 Safe YouTube Feed (Auto-Filtered)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
        st.caption("Educational Content - Safe")
        st.video("https://www.youtube.com/watch?v=6THVz8-L16U")
    with col2:
        st.video("https://www.youtube.com/watch?v=71h8MZshGSs")
        st.caption("Nursery Rhymes - Safe")
        st.video("https://www.youtube.com/watch?v=5V_2S6pW_n8")

# 5. 30 Minute Lock Feature (Simulated Footer)
st.sidebar.warning("⏳ Auto-Lock: 28/30 mins used")
if st.sidebar.button("Simulate 30 Min Lock"):
    st.error("🔒 SCREEN LOCKED: Time limit reached. Go play outside!")
    st.stop()
