from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Example text you want to summarize
text_to_summarize = """
Artificial Intelligence (AI) is transforming industries by automating processes,
improving decision-making, and enhancing customer experiences.
From chatbots to autonomous vehicles, AI applications are growing rapidly.
However, challenges such as bias, ethics, and regulation must be addressed
to ensure responsible use of the technology.
"""

# Ask GPT to summarize
response = client.chat.completions.create(
    model="gpt-4o-mini",   # good default model
    messages=[
        {"role": "system", "content": "You are a professional summarizer. Summarize text clearly and concisely."},
        {"role": "user", "content": f"Summarize this text in 3 bullet points:\n\n{text_to_summarize}"}
    ]
)

# Print summarized output
print("✅ Summary:\n")
print(response.choices[0].message.content)
