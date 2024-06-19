### Health Management App
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Function is to load the google gemini vision api and get response

def get_gemini_response(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):

    if uploaded_file is not None:

        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
st.set_page_config("Calorie Calculator")
st.header("Calorie detector")
input=st.text_input("Input",key="input")
uploaded_file=st.file_uploader("Choose and image...",type=["jpg","jpeg","png","cms","webp"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)

submit=st.button("Calculate the calories")

input_prompt=""" Your are an expert in nutritionist where you need to see the food items from the image and calculate the toal calories also provide the details of every food item in the below format

1. Item 1:- No of calories
2. Item 2:- No of calories
"""
if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The calorie chart is")
    st.write(response)
