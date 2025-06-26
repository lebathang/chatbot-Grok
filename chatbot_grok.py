from dotenv import load_dotenv
import os
import json
from openai import AsyncOpenAI
import chainlit as cl
import asyncio
import textwrap # Thêm thư viện này vào đầu file

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

# HÀM NÀY KHÔNG THAY ĐỔI
async def generate_image(prompt: str):
    try:
        # Lưu ý: Model tạo ảnh của xAI có thể có tên khác.
        # Hãy kiểm tra tài liệu để chắc chắn. "grok-2-image" chỉ là ví dụ.
        response = await xai_client.images.generate(
            model="grok-2-image", # Sử dụng một model tạo ảnh thực tế ví dụ như DALL-E 3
            prompt=prompt
        )
        return response.data[0].url if response.data else None
    except Exception as e:
        await cl.Message(content=f"Lỗi khi tạo hình ảnh: {str(e)}").send()
        return None

# SỬA ĐỔI QUAN TRỌNG: Hàm này bây giờ nhận lịch sử làm tham số
async def handle_text_query(message: str, history: list):
    # Thêm tin nhắn của người dùng vào lịch sử được truyền vào
    history.append({"role": "user", "content": message})
    
    try:
        # === LỆNH GỌI API CỦA BẠN ĐÂY ===
        # Lệnh gọi này đã được viết đúng. Model 'grok-3' có thể cần được
        response = await xai_client.chat.completions.create(
            model="grok-3", # Sử dụng model phù hợp với API của xAI
            messages=history, # Sử dụng lịch sử của phiên làm việc
            stream=False,
            **text_settings
        )
        response_content = response.choices[0].message.content
        
        # Thêm phản hồi của trợ lý vào lịch sử
        history.append({"role": "assistant", "content": response_content})
        
        # Trả về cả nội dung và lịch sử đã cập nhật
        return response_content, history
    
    except Exception as e:
        error_msg = f"Lỗi khi xử lý tin nhắn: {str(e)}"
        return error_msg, history

# xác thực người dùng
USERS_DB = {
    "user1": "password123",
    "admin": "supersecretpassword"
}

@cl.password_auth_callback
async def auth_callback(username: str, password: str) -> cl.User | None:
    """
    Hàm này được gọi khi người dùng nhập username và password.
    """
    # Kiểm tra xem username có trong "cơ sở dữ liệu" của chúng ta không
    if username in USERS_DB:
        # Lấy mật khẩu đúng
        correct_password = USERS_DB.get(username)
        # So sánh mật khẩu người dùng nhập với mật khẩu đúng
        if password == correct_password:
            # Nếu đúng, trả về một đối tượng cl.User
            # `identifier` là thông tin sẽ được dùng để nhận diện người dùng trong session.
            return cl.User(identifier=username, metadata={"role": "user"})
    
    # Nếu username không tồn tại hoặc sai mật khẩu, trả về None
    return None



# Chainlit events
@cl.on_chat_start
async def on_chat_start():
 # SỬA ĐỔI QUAN TRỌNG: Khởi tạo lịch sử và lưu vào session
 # cho từng người dùng khi họ bắt đầu chat.
 initial_history = [{"role": "system", "content": "Bạn là Grok, một chatbot hữu ích được tạo bởi xAI."}]
 cl.user_session.set("message_history", initial_history)

 elements = [
 cl.Image(
 name="image1",
 display="inline",
 path="./public/welcome.gif",
 )
]
# 1. Tạo nội dung tin nhắn với cú pháp Markdown
 note_content = ("Xin chào! Tôi là Grok, Chatbot xAI. Bạn cần giúp gì hôm nay?\n"
"""
---
 *NOTE:*
 - Gởi tin nhắn văn bản để sử dụng model xử lý văn bản Grok-3.
 - Gởi tin nhắn có chứa từ khóa `tạo hình ảnh` để sử dụng model tạo hình ảnh Grok-2-image.
 ---
"""
)
 
 # 2. Gửi tin nhắn dưới dạng NOTE
 await cl.Message(
 content=note_content,
 elements=elements # Giữ lại elements nếu bạn có sử dụng
 ).send()

# SỬA ĐỔI QUAN TRỌNG: Xử lý tin nhắn từ người dùng


@cl.on_message
async def on_message(message: cl.Message):
    user_message = message.content
    
    # Lấy lịch sử trò chuyện từ session
    history = cl.user_session.get("message_history")

    # Xử lý yêu cầu tạo hình ảnh
    if "tạo hình ảnh" in user_message.lower():
        prompt = user_message.replace("tạo hình ảnh", "").strip()
        if not prompt:
            await cl.Message(content="Vui lòng cung cấp mô tả cho hình ảnh, ví dụ: 'tạo hình ảnh một con mèo'.").send()
            return
            
        # Hiển thị thông báo loading cho hình ảnh
        loading_msg = cl.Message(content=f"Đang tạo hình ảnh cho: `{prompt}`... ⏳")
        await loading_msg.send()
        
        image_url = await generate_image(prompt)
        if image_url:
            image_element = cl.Image(url=image_url, name=prompt, display="inline")
            loading_msg.content = f"Đây là hình ảnh của bạn!"
            loading_msg.elements = [image_element]
            await loading_msg.update()
        else:
            loading_msg.content = "Không thể tạo hình ảnh. Vui lòng thử lại."
            await loading_msg.update()
        return
    
    # Xử lý tin nhắn văn bản với hiệu ứng loading
    loading_msg = cl.Message(content="Đang xử lý yêu cầu của bạn... ⏳")
    await loading_msg.send()
    
    # Gọi API Grok và cập nhật lịch sử
    response_content, updated_history = await handle_text_query(user_message, history)
    
    # Lưu lại lịch sử đã cập nhật
    cl.user_session.set("message_history", updated_history)
    
    # Cập nhật tin nhắn với kết quả từ API
    loading_msg.content = response_content
    await loading_msg.update()