import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sreejisha J Pisharody")
    content = """Hi Iam Sreejisha J Pisharody, currently pursuing MCA from Amrita Vishwa Vidypeetham. I completed my BCA from Sree Kerala Varma College. And then I got an opportunity to work at Venus Women 
    private limited as an Ecommerce catalogue and Inventory Manager. This is a portfolio to showcase my project on python which I have done in guidance with Udemy course by Ardit Aulce. The person on the image was my innstructor to this course. He helped us to build 10 realword application 
    """
    st.info(content)
