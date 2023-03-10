import streamlit as st
import PyPDF2
import openai
from io import BytesIO
import os
from text_summarizer.functions import summarize

st.title('PDF Text Extractor')

# Function to extract text from PDF
def extract_text(uploaded_file):
    with BytesIO(uploaded_file.read()) as f:
        pdf_reader = PyPDF2.PdfReader(f)
        num_pages = len(pdf_reader.pages)
        text = ""
        for page_num in range(num_pages):
            # Get the page object
            page = pdf_reader.pages[page_num]
            # Extract the text from the page
            page_text = page.extract_text()
            # Add the page text to the overall text
            text += page_text       
        return text

try:
    openai.api_key = os.getenv('OPENAI_KEY')
    if "summary" not in st.session_state:
        st.session_state["summary"] = ""
    uploaded_file = st.file_uploader('Choose a PDF file', type=['pdf'])
    text = extract_text(uploaded_file)

    if st.button("Submit", on_click=summarize, kwargs={"prompt": text}):
        pass

    if text:
        text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)
    
except Exception as e:
    st.write('There was an error =(')
