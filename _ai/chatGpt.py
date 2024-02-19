
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv(".data/sec/.env")
api_key = os.getenv('CHATGPT_K')


client = OpenAI(
    api_key=api_key
)

history = []
system_req = {
    "role": "system",
    "content": "respond as if you're explaining to a five-year-olld child"
}
history.append(system_req)


def ask(req):
    user_req = {
        "role": "user",
        "content": req
    }
    history.append(user_req)
    assistant = client.chat.completions.create(
        messages=history,
        model="gpt-3.5-turbo"
    )
    response_msg = assistant.choices[0].message
    history.append(response_msg)

    return response_msg.content


while (True):
    req = input("You: ")

    if (req.strip() == ''):
        break

    res = ask(req)
    print('\n')
    print(f'Bot: {res}')
    print('\n')
