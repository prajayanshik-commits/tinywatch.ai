import streamlit as st
import time

st.set_page_config(page_title="TinyWatch: AI Kids Shield", layout="wide")
st.title("🛡️ TinyWatch: AI-Autonomous Content Shield")

# --- SIDEBAR: Presentation Controls (Simulating the AI) ---
st.sidebar.header("🕹️ Demo Controls")
user_type = st.sidebar.radio("AI Detection Result:", ["Child (Age 7)", "Adult (Age 25)"])
dist = st.sidebar.slider("Proximity Sensor (cm):", 5, 100, 50)

# --- STEP 1: FACIAL ANALYSIS ---
st.write("### 📸 Step 1: Zero-UI Facial Scan")
cam = st.camera_input("Scanning for Age Verification...")

if cam:
    if user_type == "Child (Age 7)":
        # STEP 2 & 3: AGE ESTIMATION & ALERTS
        st.error("🚫 CHILD DETECTED")
        
        # PROXIMITY & SPEAKER LOGIC (The Nanny)
        if dist < 30:
            st.warning("🔊 SPEAKER: 'Please sit back! Your eyes need rest.'")
            st.info("🕒 Security Protocol: Screen will LOCK in 30 seconds...")
            
            # Progress Bar for the 30-second lock simulation
            bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                bar.progress(i + 1)
            st.error("🔒 SCREEN LOCKED: Maintain 30cm+ distance to resume YouTube.")
            st.stop() # This "Merges" with YouTube by killing the video stream

        # YOUTUBE MERGE (Kids Feed)
        st.subheader("📺 Intercepted Feed: YouTube Kids")
        c1, c2 = st.columns(2)
        with c1: st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
        with c2: st.video("https://www.youtube.com/watch?v=Z6_N99YvWLo")
            
    else:
        # ADULT MODE (Standard Feed)
        st.success("✅ ADULT DETECTED")
        st.subheader("📺 Standard YouTube Feed")
        c1, c2 = st.columns(2)
        with c1: st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        with c2: st.video("https://www.youtube.com/watch?v=3AtDnEC4zak")
