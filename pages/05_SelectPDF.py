import streamlit as st
import base64
from io import BytesIO
st.session_state.update(st.session_state)

def main():
    # display the upload form
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    # if a file is uploaded
    if uploaded_file is not None:
        # load the PDF file using requests and display it in the app
        pdf_data = uploaded_file.read()
        b64 = base64.b64encode(pdf_data).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{b64}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.write("Please upload a PDF file.")
if __name__ == '__main__':
    # LOGGED_IN key is defined by streamlit_login_auth_ui in the session state.
    if 'LOGGED_IN' in st.session_state and st.session_state.LOGGED_IN:
        main()
    else:
        st.write("Please login first")        