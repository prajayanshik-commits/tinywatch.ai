import streamlit as st

st.set_page_config(page_title="TinyWatch AI MVP", layout="wide")

st.title("🛡️ TinyWatch: AI Autonomous Shield")

# Sidebar for Demo Control
st.sidebar.header("Judge's Control Panel")
is_child = st.sidebar.toggle("Simulate Child Detected", value=True)

st.write("### 📸 Step 1: Scanning User")
img_file = st.camera_input("Take a photo to verify age")

if img_file:
    if is_child:
        st.error("🚫 CHILD DETECTED (Age: 6-8)")
        st.subheader("📺 Safe Feed: YouTube Kids Activated")
        st.video("https://www.youtube.com/watch?v=hq3yfQnllfQ") 
        st.info("💡 Virtual Nanny: 'Please sit back, you are too close to the screen!'")
    else:
        st.success("✅ ADULT DETECTED (Access Granted)")
        st.subheader("📺 Standard Feed: YouTube Full")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
