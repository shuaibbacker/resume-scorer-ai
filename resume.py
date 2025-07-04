import streamlit as st
import pdfplumber as pdf


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
get_score = st.sidebar.button("✅ Get Score")

# Main Area Response
st.title("Resume Scoring App")

if get_score:
    if uploaded_file is not None and job_role.strip() != "":
        # Display input summary
        st.success("Resume and Job Role received!")
        st.write(f"**Job Role:** {job_role}")
        st.write(f"**Uploaded File Name:** {uploaded_file.name}")
        
        # Placeholder: scoring logic goes here
        st.info("Scoring in progress... (connect your model here)")
    else:
        st.warning("Please upload a resume and enter a job role.")
