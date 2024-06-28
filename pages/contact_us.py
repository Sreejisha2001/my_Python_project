import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    # raw_message is without subject and other email format
    raw_message = st.text_area("Your message here")
    # message variable has everything which is in email format
    message = f"""\
Subject: New email from {user_email}

from: {user_email}
{raw_message}
"""
    button = st.form_submit_button("submit")
    print(button)
    if button:
        send_email(message)
        st.info("Your email was send successfully")
