from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make a request
response = client.chat.completions.create(
    model="gpt-4o-mini",  # fast + cheap model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write me a 2-sentence summary of AI automation."}
    ]
)

print(response.choices[0].message.content)
