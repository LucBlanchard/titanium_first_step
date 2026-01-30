import streamlit as st
import cv2

st.title("Webcam Control Panel")

# Initialize a session state variable to track if the camera is "on"
#Check the statut of camera
statut="OFF"

if 'run' not in st.session_state:
    st.session_state['run'] = False

# Layout for buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Start Camera"):
        statut="ON"
        st.session_state['run'] = True
        

with col2:
    if st.button("Stop Camera"):
        statut="OFF"
        st.session_state['run'] = False
        st.rerun()

# Placeholder for the video frame
frame_placeholder = st.empty()

# Camera logic
if st.session_state['run']:
    # 0 is usually the default built-in webcam
    video_capture = cv2.VideoCapture(0)
    
    while st.session_state['run']:
        ret, frame = video_capture.read()
        
        if not ret:
            st.error("Failed to access the webcam.")
            break
            
        # Convert BGR (OpenCV default) to RGB (Streamlit requirement)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the frame in the placeholder
        frame_placeholder.image(frame, channels="RGB")
        
    video_capture.release()
#else:
st.write(f"Camera is currently {statut}.")