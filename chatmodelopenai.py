from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()
chatbot = ChatAnthropic(model="claude-3-sonnet-20240229", api_key=os.getenv("G_KEY"))
while True:
    q = input("HELLO! :")
    if q.lower() == "exit":
        break
    print("BOT:", chatbot.invoke(q).content)
