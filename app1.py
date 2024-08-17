import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_prompt, image, user_prompt):
    try:
        response = model.generate_content([input_prompt, image[0], user_prompt])
        return response.text
    except Exception as e:
        st.error(f"Error in generating response: {str(e)}")
        return None

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        return None

# Set page config
st.set_page_config(page_title="Multilanguage Invoice Extractor", page_icon="🧾", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🧾 Invoice Extractor")
    st.markdown("""
    This app uses Gemini AI to extract information from invoices in multiple languages.
    
    How to use:
    1. Upload an invoice image
    2. Enter your question about the invoice
    3. Click 'Analyze Invoice' to get the information
    
    Supported file types: JPG, JPEG, PNG
    """)

# Main content
st.header("Multilanguage Invoice Extractor")

# File uploader
uploaded_file = st.file_uploader("Choose an invoice image...", type=["jpg", "jpeg", "png"])

# Image display and input fields
col1, col2 = st.columns([1, 1])

with col1:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Invoice", use_column_width=True)
    else:
        st.info("Please upload an invoice image")

with col2:
    user_prompt = st.text_area("What would you like to know about this invoice?", height=100)
    analyze_button = st.button("Analyze Invoice")

# Expert prompt
expert_prompt = """
You are an expert in understanding invoices. Analyze the uploaded invoice image and provide accurate information based on the user's question. If the information is not available or unclear in the image, please state that clearly.
"""

# Process the image and generate response
if analyze_button and uploaded_file is not None and user_prompt:
    with st.spinner("Analyzing the invoice..."):
        image_data = input_image_details(uploaded_file)
        if image_data:
            response = get_gemini_response(expert_prompt, image_data, user_prompt)
            if response:
                st.subheader("Analysis Result")
                st.write(response)
        else:
            st.error("Failed to process the image. Please try uploading again.")
elif analyze_button and (uploaded_file is None or not user_prompt):
    st.warning("Please upload an image and enter a question before analyzing.")

# Footer
st.markdown("---")
st.markdown("Powered by Gemini AI and Streamlit")