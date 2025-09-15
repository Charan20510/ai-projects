from anthropic import Anthropic
import os

# Initialize client (reads from environment variable by default)
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Send a message to Claude
response = client.messages.create(
    model="claude-3-5-sonnet-20240620",   # latest Claude model
    max_tokens=300,
    messages=[
        {"role": "user", "content": "Summarize AI automation in 3 bullet points."}
    ]
)

# Print Claude’s reply
print(response.content[0].text)
