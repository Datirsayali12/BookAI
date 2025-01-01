import json
import time

import streamlit as st
import pandas as pd
from helpers import content_creation, save_in_json, read_json, update_json, html_body_generation, write_html, css, \
    add_list_of_books, get_list_of_books

if "page" not in st.session_state:
    st.session_state.page = "Create Book"


def go_to_page(page_name):
    st.session_state.page = page_name




def create_content():
    if title:
        content_of_book = content_creation(title, desc).split('```json')[1].strip('\n')
        if '```' in content_of_book:
            content_of_book=content_of_book.strip('```')
        save_in_json(content_of_book)
        json_data = json.loads(read_json())
        rows = []
        for book in json_data:
            book_title = book['book_title']
            for chapter in book['chapters']:
                chapter_num = chapter['chapter_num']
                chapter_title = chapter['chapter_title']
                short_description = chapter['short_description']

                rows.append({
                    'Book Title': book_title,
                    'Chapter Number': chapter_num,
                    'Chapter Title': chapter_title,
                    'Chapter Description': short_description,

                })

        df = pd.DataFrame(rows)
        st.title("Book Content Display")
        st.data_editor(df)


def next_page():
    json_data = json.loads(read_json())[0]
    final_content=''
    for data in json_data.get("chapters", []):
        response = html_body_generation(json_data.get("book_title"), data.get('chapter_title', ''), data.get('sub_topics', ''),data.get('chapter_num', ''), data.get('short_description', ''),desc)
        split_content = response.split('```html')[1]
        if '```' in split_content:
            split_content = split_content.strip('```')
        new_content = split_content.split('<body>')[1].replace('</body>','')
        new_content=new_content.replace('```','') if '```' in new_content else new_content
        final_content=final_content+new_content

    final_html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{json_data.get("book_title")}</title>
                <link rel="stylesheet" href="https://xscientisttech.github.io/BookAI/main.css">
                
            </head>

            <body>

            <header>
            <h1>{json_data.get("book_title")}</h1>
            </header>

            {final_content}

            </body>
            </html>

            """
    st.components.v1.html(final_html, height=1000, width=1000, scrolling=True)

    html_path = write_html(json_data.get("book_title"), final_html)
    # st.markdown(f'<a href="{html_path}" target="_blank">Open HTML Page</a>', unsafe_allow_html=True)


st.title("Book-Writer")
st.header("Welcome to Book Writer")
desc=''

if st.session_state.page == "Create Book":
    title = st.text_input("Title*", placeholder="Title of book").lower()
    if ':' in title:
        title = title.replace(':', '')
    chapter_number = st.text_input("Number of Pages", placeholder="Optional")
    desc = st.text_area("Instructions:", value="Describe", placeholder="Optional")

    if st.button("Create book"):
        if title:
            progress_bar = st.progress(0)
            add_list_of_books(title)
            for percent_complete in range(101):
                time.sleep(0.05)
                progress_bar.progress(percent_complete)
            create_content()
            st.success("Content Created Successfully!")
        else:
            st.error("Title and Description are required!")

    if st.button("Next"):
        go_to_page("Next Page")


elif st.session_state.page == "Next Page":
    next_page()
    if st.button("Go Back to Create Book"):
        go_to_page("Create Book")


