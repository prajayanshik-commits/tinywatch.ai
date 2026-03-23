import streamlit as st

st.set_page_config(page_title="TinyWatch AI MVP", layout="wide")

st.title("🛡️ TinyWatch: AI Autonomous Shield")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🕹️ Judge's Demo Control")
is_child = st.sidebar.toggle("Simulate Child Detected", value=True)
is_too_close = st.sidebar.toggle("Simulate: Child Too Close (<30cm)", value=False)

st.sidebar.write("---")
st.sidebar.write("**Tech Stack:** OpenCV | MediaPipe | YouTube API")

# --- STEP 1: SCANNING ---
st.write("### 📸 Step 1: Privacy-Centric Face Scan")
img_file = st.camera_input("Scan to verify age and distance")

if img_file:
    if is_child:
        st.error("🚫 CHILD DETECTED (Age: 6-8)")
        
        # --- DISTANCE ALERT (The "Speaker" & "Nanny" logic) ---
        if is_too_close:
            st.toast("🔊 Voice Alert Triggered!")
            st.warning("⚠️ **VIRTUAL NANNY ALERT:** 'Please sit back! You are too close to the screen.'")
            # Showing a large warning icon to represent the Speaker/Alert
            st.header("📢 🛑 DISTANCE WARNING!")
        
        st.write("---")
        st.subheader("📺 Safe Feed: YouTube Kids (Multi-Video Grid)")
        
        # --- MULTI-VIDEO GRID (Step 3: API Interception) ---
        col1, col2 = st.columns(2)
        with col1:
            st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ") # Educational Video 1
            st.caption("Nursery Rhymes - Safe")
        with col2:
            st.video("https://www.youtube.com/watch?v=71h8MZshGSs") # Educational Video 2
            st.caption("Science for Kids - Safe")
            
        col3, col4 = st.columns(2)
        with col3:
            st.video("https://www.youtube.com/watch?v=6THVz8-L16U") # Educational Video 3
            st.caption("Storytelling - Safe")
        with col4:
            st.video("https://www.youtube.com/watch?v=5V_2S6pW_n8") # Educational Video 4
            st.caption("Phonics - Safe")

    else:
        st.success("✅ ADULT DETECTED (Full Access)")
        st.subheader("📺 Standard Feed")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
