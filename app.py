import streamlit as st

import base64
from langchain_ollama import OllamaLLM

# Initialize the model
llm = OllamaLLM(model="ALIENTELLIGENCE/medicalimaginganalysis")

def image_to_base64(image):
    """Converts an uploaded image to Base64 encoding."""
    image_data = base64.b64encode(image.read())
    return image_data.decode('utf-8')

st.title("Medical Image Analysis Bot")

# Layout
left, right = st.columns(2)

# Image upload section
with left:
    st.header("Upload Image")
    uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
