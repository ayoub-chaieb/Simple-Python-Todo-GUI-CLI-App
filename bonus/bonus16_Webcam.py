import streamlit as st
from PIL import Image

with st.expander('Start Camera'):
    # Start the camera
    camera_img = st.camera_input('Camera')

if camera_img:
    # Create a pillow image instance
    img = Image.open(camera_img)

    # Convert the pillow image to grayscale
    gray_img = img.convert('L')

    # Render the grayscale image on the webpage
    st.image(gray_img)