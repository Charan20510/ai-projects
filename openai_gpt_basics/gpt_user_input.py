from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# User Input
user_input = input("What's on your mind! to explore: ")

# Make a request to GPT
response = client.chat.completions.create(
    model="gpt-4",  # you can also try "gpt-4" or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
)

# Print GPT's reply
print(response.choices[0].message.content)
