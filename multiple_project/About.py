# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:09:34 2023

@author: 91879
"""
import streamlit as st

st.set_page_config(
    page_title="Multiple Disease Detection System",
    page_icon="❤️",
)



st.markdown("<h1 style='text-align: center; font-weight: bolder; font-size:100px'>HealthSewa</h1>", unsafe_allow_html=True)
st.sidebar.success("Select a page above.")

import json
import requests
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Display the header text and the provided text
st.write(
    "<div style='background-color:#DCDCDC; padding:40px; border-radius: 20px; font-style: italic; font-size: 24px;'> <img src='https://img.freepik.com/free-photo/life-insurance-concept-with-paper-family_23-2149191410.jpg?size=626&ext=jpg' style='width: 200px; height: 200px; margin-right: 20px; float: left;'>Welcome to HealthSewa, your all-in-one health companion! Our app is designed to help you take control of your health and make informed decisions about your well-being.Our mission is to empower you to live a healthier and happier life. Whether you're a fitness enthusiast, a patient managing a chronic condition, or simply looking to improve your overall well-being, HealthSewa is here to support you every step of the way.</div>",
    unsafe_allow_html=True,
)





lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_e0vedzue.json")

# Define a CSS style for the container
container_style = """
    display: flex;
"""

# Define a CSS style for the text container
text_style = """
    flex-grow: 1;
    padding: 20px;
"""

# Define a CSS style for the Lottie container
lottie_style = """
    display: flex;
    margin:0px;
    width: 100%;
"""

# Wrap the text and Lottie containers in a flexbox container
st.markdown(f'<div style="{container_style}">', unsafe_allow_html=True)

# Create the text container
st.markdown(f'<div style="{text_style}">', unsafe_allow_html=True)



# Close the text container
st.markdown('</div>', unsafe_allow_html=True)

# Create the Lottie container
st.markdown(f'<div style="{lottie_style}">', unsafe_allow_html=True)

# Display the Lottie animation
st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height=550,
    width=550,
    key=None,
)

# Close the Lottie container
st.markdown('</div>', unsafe_allow_html=True)

# Close the flexbox container
st.markdown('</div>', unsafe_allow_html=True)
