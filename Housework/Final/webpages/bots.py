from django.conf import settings
from openai import OpenAI

CLIENT = OpenAI(api_key=settings.OK)

def chatbot(r):
    r = CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": message},
        ],
    )
    return r.choices[0].message.content