from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

st.set_page_config(page_title="Positive News", page_icon=":robot:")
st.header("Positive News")

def get_text():
    input_text = st.text_area(label="News Input", label_visibility='collapsed', placeholder="Your News...", key="email_input")
    return input_text

email_input = get_text()

if len(email_input.split(" ")) > 700:
    st.write("Please enter a shorter Text. The maximum length is 700 words.")
    st.stop()

loader = YoutubeLoader.from_youtube_url("input_text", add_video_info=True)
result = loader.load()

print (type(result))
print (f"Found video from {result[0].metadata['author']} that is {result[0].metadata['length']} seconds long")
print ("")
print (result)