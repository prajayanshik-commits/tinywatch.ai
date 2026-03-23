import streamlit as st
import time

st.set_page_config(page_title="TinyWatch AI", layout="wide")

st.title("🛡️ TinyWatch: Autonomous KidShield")

# 1. Automatic Scan Area
st.write("### 📸 Face Scan to Unlock")
img_file = st.camera_input("Scan your face", label_visibility="hidden")

# Initialize Session State for Timer
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# 2. Logic after Scanning
if img_file:
    # We simulate the Age Detection logic here
    # If a face is in the camera, we trigger 'Child' mode for the demo
    is_child = True 
    
    if is_child:
        # Green Detection Label
        st.markdown("<h2 style='color: #28a745; text-align: center;'>✅ CHILD DETECTED</h2>", unsafe_allow_html=True)
        
        # Speaker Alert - Only shows if they are using the app (Child mode)
        st.markdown("""
            <div style="background-color: #ffe6e6; padding: 15px; border: 2px solid red; border-radius: 10px;">
                <h2 style='color: red; text-align: center; margin: 0;'>🔊 SPEAKER: 'Please sit back, be far from the screen!'</h2>
            </div>
            """, unsafe_allow_html=True)
        
        st.write("---")
        
        # 3. Safe YouTube Feed
        st.subheader("📺 Safe Kids Feed (Auto-Filtered)")
        col1, col2 = st.columns(2)
        with col1:
            st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ")
            st.video("https://www.youtube.com/watch?v=6THVz8-L16U")
        with col2:
            st.video("https://www.youtube.com/watch?v=71h8MZshGSs")
            st.video("https://www.youtube.com/watch?v=5V_2S6pW_n8")

    else:
        # Adult Detection Label
        st.markdown("<h2 style='color: #007bff; text-align: center;'>👤 ADULT DETECTED</h2>", unsafe_allow_html=True)
        st.info("Standard access granted. Speaker alerts disabled.")

# 4. 30 Minute Lock Logic
elapsed_time = (time.time() - st.session_state.start_time) / 60
if elapsed_time >= 30:
    st.error("🔒 SCREEN LOCKED: 30-Minute Daily Limit Reached.")
    st.stop()

st.sidebar.write(f"⏱️ Session: {elapsed_time:.1f} / 30 mins")
