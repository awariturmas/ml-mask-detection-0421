import streamlit as st
import requests
from utils.io_utils import load_config

config = load_config()

st.title("Mask detector")
url = st.text_input("Image url")

if url:
    response = requests.get(config["api"]["prediction_url"], params={"url": url})
    st.write(response.json())
