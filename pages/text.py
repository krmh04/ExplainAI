import streamlit as st
import openai
import os
from text_summarizer.functions import summarize

st.title("Summarize your text in an instant")
input_text = st.text_area(label="Enter the text:", value="", height=250)
st.button(
        "Submit",
        on_click=summarize,
        kwargs={"prompt": input_text},
    )
try:
    openai.api_key = os.getenv('OPENAI_KEY')
  
    if "summary" not in st.session_state:
        st.session_state["summary"] = ""
    
    if input_text:
        output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)
    
    
except:
    st.write('There was an error =(')
