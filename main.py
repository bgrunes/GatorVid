from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BARD_API_KEY")
bard = Bard(token=token)

# Feature to ask Google bard questions
question = input("Your question for Google Bard: ")
result = bard.get_answer(question)
content1 = result["content"]
print(content1)
print()

# Feature to find educational video about topic
topic = input("Find videos on topics you are confused about: ")
result = bard.get_answer("Find a link to a video on Youtube about " + topic)
content2 = result["content"]
print(content2)