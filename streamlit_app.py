import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from datetime import date

"""
# Welcome to BotanIQ!

# Set page title
st.title('Flower and Plant Form')

# Add input fields for name, type, and description
name = st.text_input('Name')
type = st.selectbox('Type', ['Flower', 'Plant'])
description = st.text_area('Description')

# Add date picker for date
date = st.date_input('Date', date.today())

# Add file uploader for image
image = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'])

# Add submit button
submit_button = st.button('Submit')

# Process form submission
if submit_button:
    if not name or not description:
        st.error('Please fill in all required fields.')
    else:
        st.success('Form submitted successfully!')
        st.write('Name:', name)
        st.write('Type:', type)
        st.write('Description:', description)
        st.write('Date:', date)
        if image:
            st.image(image, caption='Uploaded Image', use_column_width=True)

