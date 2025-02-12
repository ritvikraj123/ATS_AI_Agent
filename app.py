from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image
import fitz  # PyMuPDF for PDF processing
import google.generativeai as genai

# Configure the API key for Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Open the PDF with PyMuPDF (fitz)
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        first_page = pdf_document[0]  # Get the first page
        
        # Render the first page as an image
        pix = first_page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Convert the image to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        # Prepare the PDF parts for the API
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App
# Initialize session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Text area for job description
input_text = st.text_area("Job Description: ", key="input")

# File uploader for the resume
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

# Display upload success message
if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Chat-like input
user_input = st.text_input("Ask your question:", key="chat_input")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if user_input:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        
        # Select the appropriate prompt based on user input
        if submit1:
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
        elif submit3:
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
        else:
            response = get_gemini_response(user_input, pdf_content, input_text)
        
        st.subheader("Response:")
        st.write(response)

        # Add user input and response to chat history
        st.session_state.chat_history.append({"user": user_input, "bot": response})
    else:
        st.session_state.chat_history.append({"user": user_input, "bot": "Please upload the resume first."})

# Display the chat history
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**AI:** {chat['bot']}")