import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

def _get_gemini_response(input_text, image):
    if input_text != "":
        response = model.generate_content([image, input_text])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config("Vision Model")
st.header("Ask ChatGOT")

input_text = st.text_input("Input:", key='input_text')
file = st.file_uploader("Choose an image ...", type=["png", "jpg", "jpeg"])

image = None
if file is not None:
    image = Image.open(file)
    st.image(image, caption="Your file", use_column_width=True)

submit = st.button("Submit")

if submit and image is not None:
    with st.spinner(text="Processing..."):
        response = _get_gemini_response(input_text, image)
        st.subheader("ChatGOT says")
        st.write(response)
        st.success("Completed")
elif submit and image is None:
    st.warning("Please upload an image before submitting.")

