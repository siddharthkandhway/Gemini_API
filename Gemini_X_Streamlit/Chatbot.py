from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import time

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-pro')

def _get_gemini_response(user_input):
    response=model.generate_content(user_input)
    return response.text

st.set_page_config("Gemini Model ")
st.header("Ask ChatGOT")
input=st.text_input("Input:",key="input")
submit=st.button("Submit")

if submit or input:
    with st.spinner(text="Processing..."):
    
        response=_get_gemini_response(input)
        st.subheader("ChatGOT says")
        st.write(response)
        st.success('Done!')
    