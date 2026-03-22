import streamlit as st

st.set_page_config(page_title="TinyWatch AI MVP", layout="wide")

st.title("🛡️ TinyWatch: AI Autonomous Shield")
st.subheader("Real-time Age Detection & Content Filtering")

# Sidebar for "Virtual Nanny" Stats
st.sidebar.header("Virtual Nanny Dashboard")
st.sidebar.write("Status: Active 🟢")

# Mock Camera Input
img_file = st.camera_input("Scan Face to Unlock Content")

if img_file:
    st.warning("⚠️ CHILD DETECTED (Age Est: 7-9). Activating KidShield...")
    st.write("### 📺 Safe Content Feed (YouTube Kids)")
    # This is a safe educational video for the demo
    st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ") 
else:
    st.info("Please stand in front of the camera to begin.")
