# kids_fruit_ai.py

import streamlit as st
from duckduckgo_search import DDGS

from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Fruit Finder for Kids", page_icon="🍎")

st.title("🍉 AI Fruit Finder")
st.subheader("Type the name of a fruit and see pictures!")

# Input: one-word fruit name
fruit_name = st.text_input("Enter a fruit name (e.g., apple, banana):", max_chars=20)

if fruit_name:
    with st.spinner("Looking for images..."):
        with DDGS() as ddgs:
            results = list(ddgs.images(fruit_name + " fruit", max_results=5))

        if results:
            st.success(f"Here are some pictures of {fruit_name}!")
            for result in results:
                img_url = result['image']
                try:
                    response = requests.get(img_url)
                    img = Image.open(BytesIO(response.content))
                    st.image(img, use_column_width=True)
                except:
                    continue
        else:
            st.warning("Sorry, couldn't find any images!")

