import streamlit as st
from modules.login import Login
import trycourier
from streamlit_login_auth_ui.mydeta import deta_db

st.title('Welcome to ExplainAI')
def main():
    st.title("Summarize or ask questions")
    db=None
    users_auth_file = '_secret_auth_.json'
    deta_project_key=st.secrets['Deta_Project_Key']
    deta_db_name=st.secrets['Deta_Db_Name']
    db=deta_db(deta_project_key,deta_db_name)
    # users_auth_file=st.secrets['users_auth_file']
    courier_auth_token=st.secrets['courier_auth_token']
    login=Login(users_auth_file,courier_auth_token,db)
    logauth=login.login_auth()
    
    try:
        
        is_login = logauth.build_login_ui()
    except trycourier.exceptions.CourierAPIException:
        st.error('CourierAPIException, email notification might not be supported. Please try later.')
    
    if is_login:
        # Get user name.
        
            username = None
            username = logauth.get_username()
            st.markdown(f'''
            Welcome user <span style="color: white;">**{username}!**</span>
            ''',
            unsafe_allow_html=True)


if __name__ == '__main__':
    main()