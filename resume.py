import streamlit as st
import pdfplumber as pdf


# Authentication Creation

st.set_page_config(page_title="Resume scrorer Ai", layout="centered")

st.title("📄 Resume Scorer Ai")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Read the PDF
    reader = pdf(uploaded_file)
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
