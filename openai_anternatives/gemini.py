from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.Client(api_key=os.getenv("GEMINI_API_KEY"))   # or pass key directly (not recommended)
client = genai.Client()
resp = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="Write a 2-points summary of why AI automation is useful."
)
print(resp.text)
