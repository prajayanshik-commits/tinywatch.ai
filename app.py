import streamlit as st
import time

st.set_page_config(page_title="TinyWatch: Intelligent Shield", layout="wide")

# --- SIDEBAR (Hidden Logic for the Demo) ---
st.sidebar.title("🛠️ Demo Controls")
user_type = st.sidebar.radio("AI Detection Result:", ["Child", "Adult"])
# This slider represents the 'Real-time Distance' calculated by the camera
distance = st.sidebar.slider("Distance from Screen (cm):", 0, 100, 50)

st.title("🛡️ TinyWatch: Autonomous KidShield")

# --- STEP 1: AUTOMATIC SCAN ---
st.write("### 📸 Face Scan Active")
img_file = st.camera_input("Scanning...", label_visibility="hidden")

if img_file:
    # 1. Age Detection Result
    if user_type == "Child":
        st.markdown("<h2 style='color: #28a745; text-align: center;'>✅ CHILD DETECTED</h2>", unsafe_allow_html=True)
        
        # --- 2. CONDITIONAL SPEAKER LOGIC ---
        # Only show speaker if child is closer than 30cm
        if distance < 30:
            st.markdown("""
                <div style="background-color: #ffcccc; padding: 20px; border-radius: 10px; border: 3px solid red;">
                    <h2 style='color: red; text-align: center; margin: 0;'>🔊 SPEAKER: 'Please sit back, be far from the screen!'</h2>
                    <p style='text-align: center; color: black;'><b>⚠️ Proximity Alert: Eyes are too close to pixels.</b></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("📏 Safe Distance Maintained. No alerts active.")

        # --- 3. SAFE FEED ---
        st.write("---")
        st.subheader("📺 Safe Kids Feed (Auto-Filtered)")
        col1, col2 = st.columns(2)
        with col1:
            st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
        with col2:
            st.video("https://www.youtube.com/watch?v=71h8MZshGSs")

    else:
        # --- ADULT MODE ---
        st.markdown("<h2 style='color: #007bff; text-align: center;'>👤 ADULT DETECTED</h2>", unsafe_allow_html=True)
        st.info("Adult Access: Proximity monitoring and speaker alerts are currently paused.")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# 4. 30 Minute Lock Feature
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()
elapsed = (time.time() - st.session_state.start_time) / 60
if elapsed >= 30:
    st.error("🔒 SCREEN LOCKED: 30-Minute Daily Limit Reached.")
    st.stop()
