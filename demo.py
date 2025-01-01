import streamlit as st

dashboard = st.Page(
    "Home/Generate_book.py", title="Generate Book", icon=":material/dashboard:", default=True
)
all_books = st.Page("Books/all_books.py", title="All Books", icon=":material/event_list:")

generated_book = st.Page("Home/Generated_Book.py", title="Generated_Book", icon=":material/auto_stories:")


# search = st.Page("tools/search.py", title="Search", icon=":material/search:")
# history = st.Page("tools/history.py", title="History", icon=":material/history:")


pg = st.navigation(
    {
       # "Account": [logout_page],
        "Home": [dashboard, generated_book],
        "Books": [all_books],
    }
)


pg.run()