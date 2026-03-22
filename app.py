import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Set up the page matching your PPT Title
st.set_page_config(page_title="TinyWatch: AI Kids Protection", layout="wide")

# Slide 1: Title & Vision
st.title("🛡️ TinyWatch: AI-Based Kids Content Protection")
st.markdown("### *Ensuring a Safe Digital Environment using Real-time Detection*")

# Sidebar: Technical Architecture & Demo Controls
st.sidebar.header("⚙️ System Control Panel")
st.sidebar.info("Technical Architecture: OpenCV + MediaPipe + YouTube API v3")

# This toggle simulates the 'Age Estimation' (Slide 3: Step 2)
app_mode = st.sidebar.selectbox("Simulated User Detection", ["Adult (Full Access)", "Child (Restricted Mode)"])

# Interactive Voice Alert Toggle (Slide 4)
voice_alerts = st.sidebar.checkbox("Enable 'Virtual Nanny' Voice Alerts", value=True)

# Slide 3: Core Methodology - Step 1: Facial Analysis
st.write("---")
st.subheader("Step 1 & 2: Facial Analysis & Age Estimation")
img_file = st.camera_input("Scanning for User Detection (Zero-UI Friction)...")

if img_file:
    # Converting image for processing (Simulating Computer Vision)
    st.success("Face Detected: Running Deep Learning Model (CNN)...")
    
    if app_mode == "Child (Restricted Mode)":
        # Slide 2 & 3: Problem & API Interception
        st.error("🚫 CHILD DETECTED (Estimated Age: <13)")
        st.warning("Action: Forcing YouTube API to 'Made for Kids' (Category 1) Content.")
        
        # Slide 4: The Smart Speaker Integration ("The Nanny")
        if voice_alerts:
            st.info("🔊 AI Speaker: 'Hey! Please sit back, your eyes need rest.'")
        
        # Displaying Filtered Content (Step 3)
        st.write("### 📺 Safe Content Feed")
        # Example of educational/safe content
        st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ") 
        
        # Privacy-Centric Message (Slide 6)
        st.caption("Privacy Note: Real-time processing active. No images stored on disk.")
        
    else:
        # Adult Mode Logic
        st.success("✅ ADULT DETECTED")
        st.write("### 📺 Standard YouTube Feed (Full Access)")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Slide 7: Conclusion & Future Scope Footer
st.write("---")
st.caption("TinyWatch Vision: Technology should protect the future, not exploit it.")
