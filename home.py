import mysql.connector as sql
import streamlit as st
import pandas as pd

# Connect to MySQL database
conn = sql.connect(host='localhost', user='root',
                   password='password', database='factorydb')

cursor = conn.cursor()

# Custom CSS styles for the page
custom_styles = """
    <style>
        body {
            background-color: #f8f4e6;  /* Ivory */
            font-family: 'Arial', sans-serif;
            color: #2c3e50;  /* Dark Slate Gray */
        }
        .title {
            font-size: 36px;
            color: #3498db;  /* Dodger Blue */
            text-align: center;
            padding: 20px;
            margin-bottom: 30px;
            border-bottom: 2px solid #3498db;  /* Dodger Blue */
        }
        .subtitle {
            font-size: 24px;
            color: #27ae60;  /* White */
            margin-bottom: 20px;
        }
    </style>
"""

# Apply custom styles
st.markdown(custom_styles, unsafe_allow_html=True)

# Set the title with custom CSS styling using markdown
st.markdown("<h1 class='title'>Welcome to Factory Management Database</h1>",
            unsafe_allow_html=True)

# Add a subtitle with custom styling
st.markdown("<p class='subtitle'>Manage your factory efficiently!</p>",
            unsafe_allow_html=True)
