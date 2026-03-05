import requests
from dotenv import load_dotenv
from os import getenv
from langchain.chat_models import init_chat_model


load_dotenv()

model = init_chat_model(
    model='gpt-4.1-mini',
    temperature=0.1
)

response = model.invoke('Hello what is a python?')

print(response)
print(response.content)
