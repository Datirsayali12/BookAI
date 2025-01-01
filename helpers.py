import json
import os

from prompt import content_prompt, html_prompt
import openai

css = """
<style>
    body {
        font-family: 'Georgia', serif;
        background-color: #faf8f2;
        color: #3e3e3e;
        line-height: 1.8;
        padding: 20px;
        margin: 0;
    }
    header {
        background-color: #5a463b;
        color: #fff;
        padding: 15px;
        text-align: center;
        border-bottom: 2px solid #4d3b32;
    }
    header h1 {
        font-size: 2rem;
        font-weight: bold;
        margin: 0;
    }
    header h3 {
    font-size: 1rem;
    font-family: 'Georgia', serif;
    color: #fff; /* Set text color to white */
    font-weight: bold;
    margin: 0;
}

    .content {
        max-width: 850px;
        margin: 30px auto;
        padding: 25px;
        background-color: #fff;
        border: 1px solid #e0d7c6;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        page-break-inside: avoid;
    }
    blockquote {
        font-style: italic;
        color: #6b4e37;
        background-color: #f9f5ef;
        border-left: 4px solid #8a6d52;
        padding: 15px 20px;
        margin: 30px 0;
        font-size: 1.2rem;
    }
    .note, .info, .warning {
        padding: 15px;
        margin-bottom: 25px;
        border-radius: 5px;
        font-size: 1.1rem;
    }
    .note { 
        background-color: #fefaf6; 
        border-left: 5px solid #8a6d52; 
        color: #6b4e37; 
    }
    .info { 
        background-color: #f6faf6; 
        border-left: 5px solid #3b7e3b; 
        color: #2e542e; 
    }
    .warning { 
        background-color: #fff8e6; 
        border-left: 5px solid #e6a800; 
        color: #806600; 
    }
    p {
        margin: 20px 0;
        text-align: justify;
        font-size: 1.15rem;
    }
    h2, h3 {
        margin-top: 40px;
        font-weight: bold;
        color: #5a463b;
    }
    h2 {
        font-size: 2rem;
        border-bottom: 2px solid #e0d7c6;
        padding-bottom: 5px;
    }
    h3 {
        font-size: 1.5rem;
    }
</style>

"""


def content_creation(title, desc="Describe"):
    message_log = [
        {
            "role": "system",
            "content": content_prompt

        },
        {
            "role": "user",
            "content": f"title: {title}, description: {desc}"
        }
    ]
    return send_message(message_log)


def html_body_generation(title,chapter_title,sub_topics,chapter_num, short_description,desc):
    message_log = [
        {
            "role": "system",
            "content": html_prompt
        },
        {
            "role": "user",
            "content": f"title: {title},sub_topics:{sub_topics},chapter_num:{chapter_num} short_description: {short_description} chapter title:{chapter_title},instructions:{desc}"
        }
    ]

    return send_message(message_log)


def send_message(message_log, temp=0.4):
    print("openai started")
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    openai.api_key = ""
    openai.api_base = "https://api.openai.com/v1"
    openai.api_type = "open_ai"
    openai.api_version = None
    # MODELS = ["gpt-4", "gpt-4-0125-preview", "gpt-3.5-turbo", "gpt-3.5-turbo-0301","gpt-3.5-turbo-0613"]
    MODELS = ["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "gpt-3.5-turbo-0613"]

    for model_name in MODELS:
        try:
            response = openai.ChatCompletion.create(
                model=model_name,  # The name of the OpenAI chatbot model to use
                messages=message_log,  # The conversation history up to this point, as a list of dictionaries
                max_tokens=1500,  # The maximum number of tokens (words or subwords) in the generated response
                # stop=None,  # The stopping sequence for the generated response, if any (not used here)
                temperature=temp,  # The "creativity" of the generated response (higher temperature = more creative)
                top_p=0,
                frequency_penalty=0,
                presence_penalty=0,
                timeout=100
            )
            # print(response)
            # Find the first response from the chatbot that has text in it (some responses may not have text)
            for choice in response.choices:
                if "text" in choice:
                    return choice.text

                # If no response with text is found, return the first response's content (which may be empty)
            print(response.usage)
            return response.choices[0].message.content
        except Exception as e:
            print("Error: OPENAI ", e)
            return {"message": str(e)}  # Return the error message instead of raising an exception
        return {"message": "Unknown error"}


def save_in_json(chapter):
    with open("chapter.json", "w") as f:
        json.dump(chapter, f, indent=4)
    return True


def read_json():
    with open("chapter.json", "r") as f:
        file_data = json.load(f)
    return file_data


def update_json(updated_json):
    with open("updated_data.json", "w") as f:
        json.dump(updated_json, f, indent=4)


def add_list_of_books(title):
    with open(f"all_books.txt", 'a') as f:
        f.write(title + "\n")


def get_list_of_books():
    with open("all_books.txt", "r") as f:
        file_data = f.readlines()
    return file_data





def write_html(title, html_content):

    directory_path = os.path.join("BooksAI", title)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file_path = os.path.join(directory_path, f"{title}.html")

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"File successfully written to: {file_path}")
    except Exception as e:
        print(f"Error writing file: {e}")

    return file_path





def read_html(title):
    directory_path = os.path.join("BooksAI", title)

    if os.path.exists(directory_path):
        file_path = os.path.join(directory_path, f"{title}.html")

        # Check if the file exists and is not empty
        if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
            # Open the file and read its content
            with open(file_path, 'r') as file:
                content = file.read()
            return content  # Return the content as a string
        else:
            return None  # Return None if the file is empty
    else:
        return None  # Return None if the directory doesn't exist


