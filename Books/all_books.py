import json
import os

import streamlit as st
import pandas as pd
from helpers import content_creation, save_in_json, read_json, update_json, html_body_generation, write_html, css, \
    add_list_of_books, get_list_of_books

st.session_state.page = "All Books"
st.title("All Books")
book_list = get_list_of_books()

st.markdown("""
    <style>
    .card {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .card h3 {
        margin: 0;
        font-size: 20px;
        color: #333;
    }
    .card p {
        font-size: 16px;
        color: #555;
    }
    .card button {
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 15px;
                font-size: 14px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
    </style>
    """, unsafe_allow_html=True)
new_list = []
for root, directory, files in os.walk('BooksAI'):
    for title in directory:
        folder_path = os.path.join(root, title)
        total_files = len([file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))])

        if title.lower() not in new_list:
            new_list.append(title)
            st.markdown(f'<div class="card"><h3>{title}</h3><p>Total chapters: {total_files} files</p></div>',
                        unsafe_allow_html=True)