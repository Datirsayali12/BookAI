import json
import time

import streamlit as st
import pandas as pd
from Home.Generate_book import desc
from helpers import content_creation, save_in_json, read_json, html_body_generation, write_html, css, add_list_of_books,read_html


progress_bar = st.progress(0)

for percent_complete in range(101):
    time.sleep(0.08)
    progress_bar.progress(percent_complete)

json_data = json.loads(read_json())[0]
title = json_data.get("book_title").replace(':', '')
# file=read_html(title)
# if not file:
final_content = ''
for data in json_data.get("chapters", []):
    response = html_body_generation(title, data.get('chapter_title', ''),
                                    data.get('sub_topics', ''), data.get('chapter_num', ''),
                                    data.get('short_description', ''),desc)
    split_content = response.split('```html')[1]
    if '```' in split_content:
        split_content = split_content.strip('```')
    new_content = split_content.split('<body>')[1].replace('</body>', '')
    new_content = new_content.replace('```', '') if '```' in new_content else new_content
    final_content = final_content + new_content

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

html_path = write_html(title, final_html)
# st.components.v1.html(file, height=1000, width=1000, scrolling=True)

