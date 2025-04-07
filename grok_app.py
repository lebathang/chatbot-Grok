from openai import OpenAI
from langchain_xai import ChatXAI
import base64
import os

XAI_API_KEY = "xai-fOhkWf2rEFWaIDc9AgKI6utjWiWF3ZnzyTIeEb6DApptHBE4SUYYb2nGmDaQOHwnzC2uMTT6flwzS7nX"
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

# 1. Basic Chat
response = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "system", "content": "You are Grok, a helful chatbot."},
        {"role": "user", "content": "Give me a meal plan for me today"},
    ],
)
print(response.choices[0].message.content)

# 2. Stream Chat
response = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "system", "content": "You are Grok, a helful chatbot."},
        {"role": "user", "content": "Give me a meal plan for me today"},
    ],
    stream=True,
)

for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

# 2 - Chat with Image
IMAGE_PATH = "triangle.png"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image(IMAGE_PATH)

response = client.chat.completions.create(
    model="grok-vision-beta",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that responds in Markdown. Help me with my math homework!"},
        {"role": "user", "content": [
            {"type": "text", "text": "What's the area of the triangle?"},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}
            }
        ]}
    ],
    temperature=0.0,
)

print(response.choices[0].message.content)

# 3. Chat with Image URL
response = client.chat.completions.create(
    model="grok-vision-beta",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that responds in Markdown. Help me with my math homework!"},
        {"role": "user", "content": [
            {"type": "text", "text": "What's the area of the triangle?"},
            {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e2/The_Algebra_of_Mohammed_Ben_Musa_-_page_82b.png"}
            }
        ]}
    ],
    temperature=0.0,
)
print(response.choices[0].message.content)

# 4. Chat Using Langchain 
response = ChatXAI(
    model="grok-beta",
)

for m in response.stream("Give me a meal plan for me today"):
    print(m.content, end="", flush=True)