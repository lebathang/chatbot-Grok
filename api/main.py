from dotenv import load_dotenv
import os
import json
from openai import AsyncOpenAI
import chainlit as cl
import asyncio

# Load environment variables
load_dotenv()

# Get the xAI API key
XAI_API_KEY = os.getenv("XAI_API_KEY")

if not XAI_API_KEY:
    raise ValueError("No valid XAI_API_KEY set. Please set it in .env.")

# Initialize xAI client
xai_client = AsyncOpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

# Text model settings
text_settings = {
    "temperature": 0.7,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

# Store message history per session
message_history = [{"role": "system", "content": "Bạn là Grok, một chatbot hữu ích được tạo bởi xAI, hỗ trợ trả lời bằng tiếng Việt hoặc tiếng Anh tùy theo yêu cầu của người dùng."}]

async def generate_image(prompt: str):
    try:
        response = await xai_client.images.generate(
            model="grok-2-image-1212",
            prompt=prompt
        )
        return response.data[0].url if response.data else None
    except Exception as e:
        await cl.Message(content=f"Lỗi khi tạo hình ảnh: {str(e)}").send()
        return None

async def handle_text_query(message: str):
    global message_history
    
    # Append user message to history
    message_history.append({"role": "user", "content": message})
    
    try:
        stream = await xai_client.chat.completions.create(
            model="grok-2-1212",
            messages=message_history,
            stream=False,
            **text_settings
        )
        response_content = stream.choices[0].message.content
        
        # Append assistant response to history
        message_history.append({"role": "assistant", "content": response_content})
        
        return response_content
    
    except Exception as e:
        error_msg = f"Lỗi khi xử lý tin nhắn: {str(e)}"
        await cl.Message(content=error_msg).send()
        return error_msg

# Chainlit events
@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Xin chào! Tôi là Grok, bot của xAI. Bạn cần giúp gì hôm nay?").send()

@cl.on_message
async def on_message(message: cl.Message):
    user_message = message.content
    
    # Kiểm tra yêu cầu tạo hình ảnh
    if "tạo hình ảnh" in user_message.lower():
        prompt = user_message.replace("tạo hình ảnh", "").strip()
        if not prompt:
            await cl.Message(content="Vui lòng cung cấp mô tả cho hình ảnh, ví dụ: 'tạo hình ảnh một con mèo'.").send()
            return
            
        await cl.Message(content="Đang tạo hình ảnh...").send()
        image_url = await generate_image(prompt)
        if image_url:
            await cl.Message(content=f"Hình ảnh của bạn: ![Generated Image]({image_url})").send()
        else:
            await cl.Message(content="Không thể tạo hình ảnh. Vui lòng thử lại.").send()
        return
    
    # Xử lý tin nhắn văn bản
    response = await handle_text_query(user_message)
    await cl.Message(content=response).send()

if __name__ == "__main__":
    cl.run()