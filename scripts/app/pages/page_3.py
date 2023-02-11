import streamlit as st
from .helpers.return_random_number import return_some_number

# Set page title
st.set_page_config(
    page_title="Final",
)

st.text(f"Some random number {return_some_number()}")
