import streamlit as st
from utils import parse_pdf, embed_text, get_answer
st.session_state.update(st.session_state)

def main():
    st.header("Ask anything about your PDF")
    uploaded_file = st.file_uploader("Upload a pdf", type=["pdf"])

    if uploaded_file is not None:
        
        index = embed_text(parse_pdf(uploaded_file))
        query = st.text_area("Ask a question about the document")
        button = st.button("Submit")
        if button:
            st.write(get_answer(index, query))
if __name__ == '__main__':
    # LOGGED_IN key is defined by streamlit_login_auth_ui in the session state.
    if 'LOGGED_IN' in st.session_state and st.session_state.LOGGED_IN:
        main()
    else:
        st.write("Please login first")