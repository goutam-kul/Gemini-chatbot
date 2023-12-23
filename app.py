
from dotenv import load_dotenv

load_dotenv() 

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai

# from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

#initialize streamlit 

st.set_page_config(page_title="Q&A Demo")
st.title('GEMINI CHAT BOT')

st.markdown("---")
user_input=st.text_input("Ask a question: ",key="user_input")
submit=st.button("Submit")


if submit:
    
    response=get_gemini_response(user_input)
    st.write(response)
