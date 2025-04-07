from dotenv import load_dotenv
import os
import json
from openai import AsyncOpenAI
import aiohttp
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64

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

# Initialize FastAPI app (suitable for Vercel)
app = FastAPI()

# Model to receive message data
class MessageRequest(BaseModel):
    content: str
    elements: list = None  # For image data if any

# Store message history per session (simplified, in reality use a database)
message_history = [{"role": "system", "content": "You are Grok, a helpful chatbot built by xAI."}]

async def generate_image(prompt: str):
    try:
        response = await xai_client.images.generate(
            model="grok-2-image-1212",
            prompt=prompt
        )
        return response.data[0].url
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

async def edit_image(image_data: str, prompt: str):
    try:
        # Decode base64 image data if provided
        image_binary = base64.b64decode(image_data.split(',')[1] if ',' in image_data else image_data)
        
        response = await xai_client.images.edit(
            model="grok-2-image-1212",
            image=image_binary,
            prompt=prompt
        )
        return response.data[0].url
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error editing image: {str(e)}")

@app.post("/chat")
async def handle_chat(message_request: MessageRequest):
    global message_history
    
    # Append user message to history
    message_history.append({"role": "user", "content": message_request.content})
    
    response_content = ""
    
    # Check if user requests image generation or editing
    if "tạo hình ảnh" in message_request.content.lower():
        prompt = message_request.content.replace("tạo hình ảnh", "").strip()
        image_url = await generate_image(prompt)
        response_content = f"![Generated Image]({image_url})"
        
    elif "xử lý hình ảnh" in message_request.content.lower() and message_request.elements:
        # Assume first element is an image (base64 encoded for simplicity)
        if not any(elem.get("type") == "image" for elem in message_request.elements):
            raise HTTPException(status_code=400, detail="No image provided for editing.")
        
        image_element = next(elem for elem in message_request.elements if elem.get("type") == "image")
        image_data = image_element.get("data")  # Expecting base64 string
        
        if not image_data:
            raise HTTPException(status_code=400, detail="Image data is missing.")
        
        prompt = message_request.content.replace("xử lý hình ảnh", "").strip()
        image_url = await edit_image(image_data, prompt)
        response_content = f"![Edited Image]({image_url})"
    
    else:
        # Handle text response
        try:
            stream = await xai_client.chat.completions.create(
                model="grok-2-1212",
                messages=message_history,
                stream=False,  # Vercel doesn't support streaming, so get all at once
                **text_settings
            )
            response_content = stream.choices[0].message.content
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")
    
    # Append assistant response to history
    message_history.append({"role": "assistant", "content": response_content})
    
    return {"response": response_content, "message_history": message_history}

# Vercel requires a handler for serverless functions
def handler(event, context):
    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        message_request = MessageRequest(**body)
        import asyncio
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(handle_chat(message_request))
        return {
            'statusCode': 200,
            'body': json.dumps(response),
            'headers': {'Content-Type': 'application/json'}
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Only POST requests are supported'})
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)