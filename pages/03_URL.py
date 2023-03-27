import streamlit as st
import openai
import os
from text_summarizer.functions import summarize
import scraper as scr
st.session_state.update(st.session_state)
def main():
    st.title("Summarize the text from any URL")

    try:
        openai.api_key = os.getenv('OPENAI_API_KEY')

        if "summary" not in st.session_state:
            st.session_state["summary"] = ""

        input_url = st.text_area(label="Enter the url:", value="", height=1)
        st.button(
        "Submit",
        on_click=summarize,
        kwargs={"prompt":  input_url},
    )
        if input_url:
            scraper = scr.Scraper()
            response = scraper.request_url(input_url) 
            url_text = (
                scraper.extract_content(response)[:6000].strip().replace("\n", " ")
            )
            url_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)

    except Exception as e:
        st.write('There was an error =(')
        st.write(e)
if __name__ == '__main__':
    # LOGGED_IN key is defined by streamlit_login_auth_ui in the session state.
    if 'LOGGED_IN' in st.session_state and st.session_state.LOGGED_IN:
        main()
    else:
        st.write("Please login first")