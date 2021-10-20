import pyrebase
import streamlit as st
from datetime import datetime

firebaseConfig = {
    "apiKey": "AIzaSyAGNesDJemnj-UmDDxBnEVjIMfRNyJleq8",
    "authDomain": "painless-app.firebaseapp.com",
    "projectId": "painless-app",
    "databaseURL": "https://painless-app-default-rtdb.europe-west1.firebasedatabase.app",
    "storageBucket": "painless-app.appspot.com",
    "messagingSenderId": "330214106315",
    "appId": "1:330214106315:web:9f13b60ceacab9d04b674e",
    "measurementId": "G-7MQEMPB7DP"
}

# firebase authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# initialize database
db = firebase.storage()
storage = firebase.storage()

st.sidebar.title("Our community app")

# Authentication
choice = st.sidebar.selectbox('Login/Signup', ['Login', 'Signup'])
email = st.sidebar.text_input('Please enter email address')
password = st.sidebar.text_input('Please enter your password', type="password")

if choice == 'Signup':
    handle = st.sidebar.text_input('Please input your app handle name', value='Default')
    submit = st.sidebar.button('Create my account')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is created successfully')
        st.balloons()
        # Sign in
        user = auth.sign_in_with_email_and_password(email, password)
        # creating database
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title('Welcome {handle}')
        st.info('Login via login drop down select')
