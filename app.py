import streamlit as st
from PyPDF2 import PdfReader
import ollama

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def analyze_cv(cv_text):
    prompt = f"Analyze this CV and provide constructive feedback to improve it:\n\n{cv_text[:2000]}"
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

st.title("CV Analyzer with Mistral (Offline)")

uploaded_file = st.file_uploader("Upload your CV (PDF format)", type=["pdf"])

if uploaded_file is not None:
    cv_text = extract_text_from_pdf(uploaded_file)
    if not cv_text.strip():
        st.error("Could not extract text from the PDF. Please upload a valid CV.")
    else:
        with st.spinner("Analyzing your CV..."):
            feedback = analyze_cv(cv_text)
        st.subheader("Analysis Feedback")
        st.write(feedback)
