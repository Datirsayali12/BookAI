content_prompt = """  I want you to act as a creative writer and structure your output in valid JSON format.
              I will provide the title and instructions and based on that you need to create table of content in the following json format.

              ```json

              [
                {
                  "book_title": "Book Title",
                  "chapters": [
                    {
                      "chapter_num": "Chapter Number should always be numeric",
                      "chapter_title": "Title of the chapter",
                      "short_description": "A short description of the chapter, to give context about what it will cover",

                      "sub_topics": [
                        {
                          "topic_name": "The name of the first subtopic or section",
                          "short_description": "A short description of what the subtopic will discuss"
                        },
                        {
                          "topic_name": "The name of the second subtopic or section",
                          "short_description": "A short description of what the subtopic will discuss"
                        }
                      ]
                    },
                    {
                      "chapter_num": "Chapter Number 2",
                      "chapter_title": "Another Chapter",
                      "short_description": "Description for another chapter.",
                      "sub_topics": [
                        {
                          "topic_name": "Subtopic 1",
                          "short_description": "Description for subtopic 1."
                        }
                      ]
                    }
                  ]
                }
              ]

              ```

              ### Instructions:
              - Generate table of content as per the given instructions and you can generate N number of chapters as required.
              - Do not create the redundant content.
              - Create sub topics only if its required otherwise leave it empty array [].
              - Make sure you are following all the user guidelines if mentioned in the instructions.
              - Ensure that each chapter must be detailed , self-explanatory, and user-centric.
                Each description should thoroughly cover the user's needs while exploring the subject in greater depth to provide a richer, more informative explanation.

           """

html_prompt = """
                ---
                
                ### Instructions for Generating Chapter Content in Plain HTML:
                Do not use section within section
                
                1. **Chapter Title**:
                   Begin with the chapter title using the `<h3>` tag and chapter number.
                   - Each chapter should be within section.
                  - Provide the chapter's content, formatted as proper html Key points, facts, or concepts related to the chapter and all possible things to cover the chapter.
                  - Any examples, anecdotes, or illustrations (as text) to make the chapter more relatable. Use appropriate tags to structure the content logically.
                
                
                2. If the chapter contains subtopics:
                     - **Subtopic Title**: Use an appropriate header (e.g., `<h2>`) for each subtopic. Ensure the subtopic name is clear and relevant.
                     - **Subtopic Content**: For each subtopic, generate a detailed content. This content should include:
                       - Key points, facts, or concepts related to the subtopic and all possible things to cover the topic.
                       - Any examples, anecdotes, or illustrations (as text) to make the topic more relatable.
                       - A concluding sentence or paragraph summarizing the subtopic’s key takeaways.
                       - Use proper HTML tags such as `<p>` for paragraphs, `<ul>` and `<li>` for lists, and `<blockquote>` for quotes if applicable.
                3. If the chapter does not contain subtopics:
                        Create a detailed description based on the chapter title. The content should include:
                        An in-depth explanation of the chapter's theme or concept.
                        Important facts, key points, or principles related to the title.
                        Any illustrative examples, anecdotes, or context to make the content engaging and relatable.              
                4. **Conclusion**:
                   Optionally, end the chapter with a conclusion or a summary that ties the main ideas of the chapter together. This should be a brief section that reinforces the key messages covered in the chapter. Use `<p>` to format this section.
                
                5. **HTML Structure**:
                   - Use heading tags (`<h2>`, `<h3>`, etc.) for subtopics and key sections within the chapter.
                   - Use appropriate tags to structure the content for readability: paragraphs (`<p>`), lists (`<ul>`, `<li>`), and any other relevant HTML elements.
                   - When creating tables as per user instructions, ensure the use of <table> for the table structure, <thead> for the header row, <tbody> for the body content, <tr> for table rows, and <td> or <th> for table cells. 
                    The table should be well-organized and properly formatted for clarity.
                   -  Use <img> to include images. Always provide the src attribute for the image source and the alt attribute for accessibility and context. 
                      Images should complement the content and enhance user understanding of the subject.
                
                6. **No CSS or styling should be included**. Only the necessary HTML structure should be generated.
                
                7. **Allowed HTML Tags**:
                   - Document Structure Tags: `<section>`, `<article>`, `<div>`, `<span>`
                   - Text Formatting Tags: `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`, `<p>`, `<b>`, `<i>`, `<u>`, `<strong>`, `<em>`, `<mark>`, `<small>`, `<sub>`, `<sup>`, `<blockquote>`
                   - List Tags: `<ul>`, `<ol>`, `<li>`, `<dl>`, `<dt>`, `<dd>`
                   - Table Tags: `<table>`, `<tr>`, `<td>`, `<th>`, `<thead>`, `<tbody>`, `<tfoot>`, `<caption>`, `<col>`, `<colgroup>`
                   - Miscellaneous Tags: `<hr>`, `<br>`, `<details>`, `<summary>`
              
                8 . Strictly follow users instructions to generate description.
                9 . Each chapter should be detailed, descriptive, and self-contained, thoroughly covering the assigned topic.
                    The content must include explanations, examples, anecdotes, and visual aids (e.g., tables and images) to ensure clarity and user engagement.

                ---
                
                Output:
                
                ```html
                
                <body>
                
                </body>
                
                ```
"""

