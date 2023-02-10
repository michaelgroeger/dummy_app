import numpy as np
import streamlit as st
from st_pages import Page, show_pages
from helpers.return_random_number import return_some_number
# Set name of current page
st.set_page_config(
    page_title="Hello",
)
# Specify what pages should be shown in the sidebar, and what their titles
# and icons should be
show_pages(
    [
        Page("main_page.py", "Hello"),
        Page("pages/page_2.py", "Next"),
        Page("pages/page_3.py", "Final"),
    ]
)
# Display title in app
st.title(
    "Welcome to the awesome gaming recommendation app, we are setting everything up for your visit"
)

st.text(f"Some random number {return_some_number()}")
