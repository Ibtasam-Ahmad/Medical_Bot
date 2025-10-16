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

with right:
    st.header("Generated Report")

    if uploaded_image is not None:
        # Show the "Generating report..." message while the report is being generated
        with st.spinner("Generating report..."):
            # Convert uploaded image to base64
            base64_string = image_to_base64(uploaded_image)

            # Pass image to the LLM and generate a report
            llm_with_image_context = llm.bind(images=[base64_string])
            report = llm_with_image_context.invoke("You are an Advanced AI Medical Imaging Analysis Service.  Using superintelligent agents to analyze medical images, detect anomalies, and provide a detail report for the respective image provided. Dont write age, gender, Image Type etc.")

            st.write(report)
    else:
        st.write("Please upload an image to generate a report.")



# OPENAI

# import streamlit as st
# import base64
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage

# # Initialize the OpenAI model
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# def image_to_base64(image):
#     """Converts an uploaded image to Base64 encoding."""
#     image_data = base64.b64encode(image.read())
#     return image_data.decode('utf-8')

# st.title("Medical Image Analysis Bot")

# # Layout
# left, right = st.columns(2)

# # Image upload section
# with left:
#     st.header("Upload Image")
#     uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

# with right:
#     st.header("Generated Report")

#     if uploaded_image is not None:
#         # Show the "Generating report..." message while the report is being generated
#         with st.spinner("Generating report..."):
#             # Convert uploaded image to base64
#             base64_string = image_to_base64(uploaded_image)

#             # Create a HumanMessage with the base64-encoded image
#             human_message = HumanMessage(
#                 content="You are an Advanced AI Medical Imaging Analysis Service. Using superintelligent agents to analyze medical images, detect anomalies, and provide a detailed report for the respective image provided. Don't write age, gender, image type, etc.",
#                 image=base64_string
#             )

#             # Generate the report
#             report = llm.invoke([human_message])

#             st.write(report)
#     else:
#         st.write("Please upload an image to generate a report.")
