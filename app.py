import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

while True:

    topic = input("\nEnter a topic: ")

    if topic.lower() == "exit":
        break

    prompt = f"""
    Explain the following topic like I'm 5 years old:

    {topic}
    """

    response = model.generate_content(prompt)

    print("\nAnswer:\n")
    print(response.text)