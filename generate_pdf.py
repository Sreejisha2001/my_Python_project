import pandas
import pandas as pd
import streamlit as st
# to read csv files
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_text_color(100,100,100)
        self.set_font("Arial","B",42)
        self.cell(0,10,self.current_title,0,10,'c')

    def footer(self):
        self.set_y(-15) # Move to 15mm from the bottom
        self.set_text_color(100,100,100)
        self.set_font("Arial",'I',8)
        self.cell(0,10,f'Page{self.page_no()}',0,0,'c')

    #def chapter_title(self, title):
     #   self.set_font("Arial",'B',12)
      #  self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self,body):
        self.set_text_color(100,100,100)
        self.set_font("Arial",'', 20)
        self.multi_cell(0, 10, body)

    def chapter_image(self,image_path):
        self.image(image_path,w=100)
        self.ln()

    def add_link(self,link):
        self.set_text_color(0,0,255)
        self.set_font('Arial', 'U', 12)
        self.cell(0,10,link,0,1,'',link)

def generate_pdf():
    pdf=PDF()
    pdf.alias_nb_pages()
    df = pd.read_csv("data.csv", sep=";")

    for index, row in df.iterrows():
        pdf.current_title=str(row["title"])
        pdf.add_page()
        pdf.chapter_body(row["description"])
        pdf.chapter_image("images/"+row["image"])
        pdf.add_link(row["url"])

    return pdf.output(dest="S").encode("latin1")

