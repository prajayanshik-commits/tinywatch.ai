import streamlit as st
import time

# 1. Setup the Page Layout
st.set_page_config(page_title="TinyWatch: AI Kids Shield", layout="wide")

st.title("🛡️ TinyWatch: AI-Autonomous Content Shield")
st.markdown("---")

# 2. Sidebar for Presentation Logic (The "Brain" of the AI)
st.sidebar.header("🕹️ Demo Controller")
user_age = st.sidebar.radio("AI Detection Result:", ["Child (Age 7)", "Adult (Age 25)"])
dist = st.sidebar.slider("Proximity Sensor (cm):", 5, 100, 50)

# 3. Facial Analysis Step
st.write("### 📸 Step 1: Zero-UI Facial Scan")
cam_input = st.camera_input("Scanning for Age Verification...")

if cam_input:
    if user_age == "Child (Age 7)":
        st.error("🚫 CHILD DETECTED")
        
        # 4. Proximity & Virtual Nanny Logic
        if dist < 30:
            st.warning("🔊 SPEAKER: 'Please sit back! You are too close.'")
            st.info("🕒 Security Protocol: Locking screen in 30 seconds if posture doesn't improve.")
            
            # Simulated Lock
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
            st.error("🔒 SCREEN LOCKED: Maintain 30cm+ distance to resume.")
            st.stop() # Prevents YouTube from loading

        # 5. YouTube API Merge (Kids Feed)
        st.subheader("📺 Intercepted Feed: YouTube Kids")
        col1, col2 = st.columns(2)
        with col1:
            st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ") # Educational Video
        with col2:
            st.video("https://www.youtube.com/watch?v=Z6_N99YvWLo") # Moral Stories
            
    else:
        # Adult Mode
        st.success("✅ ADULT DETECTED")
        st.subheader("📺 Standard YouTube Feed")
        col1, col2 = st.columns(2)
        with col1:
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Standard Content
        with col2:
            st.video("https://www.youtube.com/watch?v=3AtDnEC4zak") # Tech News
