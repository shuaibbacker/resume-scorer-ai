import streamlit as st
import pdfplumber as pdf
import os
from dotenv import load_dotenv
import requests

load_dotenv()

# configure the Gemini API

API_KEY = os.getenv("GEMINI_API")

GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Function for gemini Api

def get_gemini_response(input_text):
    headers = {

        'Content-Type': "application/json"
    }
    data = {
        "contents": {
            {
                "parts": [
                    {
                        "text": input_text
                    }
                ]
            }
        }
    }
    response = requests.post(GEMINI_URL, headers=headers, json=data)

    if response.status_code==200:
        result = response.json()
        return result['candidates'][0]['contents']['parts'][0]['text']
    else:
        return f"API Error: {response.status_code} - {response.text}"
    
# Authentication Creation

st.set_page_config(page_title="Resume scrorer Ai", layout="centered")

st.title("📄 Resume Scorer Ai")

# Sidebar Elements
st.sidebar.title("Resume Analyzer")

# Upload Resume
uploaded_file = st.sidebar.file_uploader("📄 Upload a PDF File", type="pdf")

if uploaded_file is not None:

# Read the PDF
    reader = pdf.open(uploaded_file)
    num_pages = len(reader.pages)

    st.success(f"Uploaded PDF with {num_pages} page(s).")

    # Optional: Display the text content of all pages
    text = ""
    for i, page in enumerate(reader.pages):
        text += page.extract_text() or ""
    
    if text:
        st.subheader("Extracted Text:")
        st.text_area("Text Content", text, height=300)
    else:
        st.warning("No extractable text found in this PDF.")

# Enter Job Role
job_role = st.sidebar.text_input("💼 Enter Job Role")

# Get Score Button

if st.sidebar.button("✅ Get Score"):
    with st.spinner("Analyzing.."):
        prompt = f"Analyze the extracted text:\n{text}, and job role:\n{job_role}. According to job role and text calculate the score out of 1-10 and only show the calculated score without showing entire text. and suggest changes to make a resume perfect score"
        response = get_gemini_response(prompt)
        st.subheader(f"The resume Score: {response} out of 10")


# # Main Area Response
# st.title("Resume Scoring App")

# if get_score:
#     if uploaded_file is not None and job_role.strip() != "":
#         # Display input summary
#         st.success("Resume and Job Role received!")
#         st.write(f"**Job Role:** {job_role}")
#         st.write(f"**Uploaded File Name:** {uploaded_file.name}")
        
#         # Placeholder: scoring logic goes here
#         st.info("Scoring in progress... (connect your model here)")
#     else:
#         st.warning("Please upload a resume and enter a job role.")
