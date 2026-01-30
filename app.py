import streamlit as st
import cv2

st.title("Webcam Control Panel")

# 1. Initialize session state
if 'run' not in st.session_state:
    st.session_state['run'] = False

# 2. Camera Status UI
if st.session_state['run']:
    st.success("STATUS: **ON**")
else:
    st.error("STATUS: **OFF**")

# Layout for buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Start Camera", use_container_width=True):
        if not st.session_state['run']:
            st.session_state['run'] = True
            st.rerun() 

with col2:
    if st.button("Stop Camera", use_container_width=True):
        if st.session_state['run']:
            st.session_state['run'] = False
            st.rerun()

# Placeholder for the video frame
frame_placeholder = st.empty()

# 3. Camera Logic
if st.session_state['run']:
    cap = cv2.VideoCapture(0)
    
    while st.session_state['run']:
        ret, frame = cap.read()
        if not ret:
            st.warning("Webcam not found. Check connections.")
            st.session_state['run'] = False
            break
            
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")
    
    cap.release()
else:
    frame_placeholder.info("Click 'Start Camera' to begin the stream.")