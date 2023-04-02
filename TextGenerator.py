

import openai
openai.api_key = "enter key here"

def generate_text(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    message = completion["choices"][0]["message"]["content"]
    return message


