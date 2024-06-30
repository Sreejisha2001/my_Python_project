import pandas
import streamlit as st
from fpdf import FPDF
from generate_pdf import generate_pdf

# to read csv files

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
content=""" Below you can find some of the apps 
i have built in python. Feel free to contact me. You can find my contact details on this following link i have given here. Thank you !!!"""
st.write(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df=pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})") #can add github link of each project

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})") #can add github link of each project


#add button to generate pdf
if st.button("Generate PDF"):
    pdf_data=generate_pdf()
    st.download_button(label="download pdf", data=pdf_data, file_name="project.pdf", mime="application/pdf")

