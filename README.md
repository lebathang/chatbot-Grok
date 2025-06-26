# Chào mừng đến với chatbot Grok 🚀🤖

Xin chào mọi người 👋 Hôm nay mình chia sẻ, hướng dẫn cài đặt và sử dụng con chatbot này, mặc dù còn đang phát triển nhưng tôi hy vọng mọi người sẽ thích và đóng góp nó 🥰

## Hướng Dẫn Cài Đặt ⚙️

### 1. Clone Repository
```bash
git clone https://github.com/lebathang/chatbot-Grok.git
cd chatbot-Grok
```
### 2.Cài Đặt Phụ Thuộc
Cài đặt các thư viện cần thiết bằng cách chạy:
```bash
pip install -r requirements.txt
```
### 3. Chạy Dự Án
Khởi động ứng dụng bằng lệnh:
```bash
chainlit run chatbot_grok.py -w
```
Mở trình duyệt và truy cập http://localhost:8000 để sử dụng.

## Giới thiệu - Hướng dẫn sử dụng 📖

- **API key:** trước tiên phải chuẩn bị api key Grok thì bạn phải vào [console.x.ai](https://console.x.ai/) để lấy API key 🔑

![img](https://i.ibb.co/dwJZZh5R/WUBKYCTQASEVYSC.jpg)

- **Model xử lý văn bản (Language Models):** Tôi sử dụng model **Grok 3** cho xử lý các tác vụ liên quan đến văn bản, text. Đây là một mô hình ngôn ngữ lớn (LLM) thế hệ tiếp theo, được thiết kế để vượt trội trong nhiều lĩnh vực, từ xử lý văn bản chuyên sâu đến các tác vụ đa phương thức (multimodal) trong tương lai. Grok 3 được cải tiến đáng kể về khả năng suy luận, hiểu ngữ cảnh và hiệu suất so với các phiên bản tiền nhiệm như Grok-2.

    - Cung cấp khả năng suy luận logic và giải quyết vấn đề ở cấp độ cao, vượt trội hơn các phiên bản trước.
    - Xử lý các tài liệu dài và phức tạp một cách hiệu quả nhờ vào cửa sổ ngữ cảnh lớn.
    - Thể hiện sự hiểu biết sâu sắc về các lĩnh vực chuyên môn như toán học, lập trình và khoa học.

        + **Dung lượng ngữ cảnh:** 128K token, tương đương với Grok-2, cho phép xử lý và phân tích các đoạn hội thoại dài hoặc khối lượng văn bản lớn một cách liền mạch.

        + **Hiệu suất và điểm chuẩn:** Grok 3 đã cho thấy hiệu suất vượt trội so với các mô hình cùng phân khúc như GPT-4 và Claude 3 Opus trên nhiều bài kiểm tra tiêu chuẩn, bao gồm các bài toán, lập trình và kiến thức tổng quát.

        + **Tầm nhìn tương lai:** Mặc dù phiên bản hiện tại tập trung vào văn bản, Grok 3 được xây dựng với kiến trúc hướng tới khả năng đa phương thức, hứa hẹn sẽ sớm hỗ trợ xử lý hình ảnh, âm thanh và video.

        ⇒ **Grok 3** là lựa chọn hàng đầu cho các tác vụ đòi hỏi khả năng suy luận phức tạp, độ chính xác cao và khả năng xử lý ngữ cảnh dài, thiết lập một tiêu chuẩn mới về hiệu suất trong lĩnh vực trí tuệ nhân tạo.

![img](/public/test_text.png)

- **Model tạo hình ảnh (Image Generation Models):** Ở đây tôi sử dụng model **Grok-2-image-1212** để tạo hình ảnh. Dựa trên thông tin từ web, Grok 2 nói chung (bao gồm các phiên bản như **Grok-2-image-1212**) có thể xử lý các prompt phức tạp hơn nếu được cung cấp chi tiết cụ thể và rõ ràng. **Grok-2-image-1212** là mô hình chuyên biệt để tạo hình ảnh, sử dụng FLUX.1, với khả năng tạo hình ảnh chi tiết và chân thực, nhưng có hệ thống kiểm duyệt nội dung rất nhạy. ✏️


    - **Giá cả:** Giá của **Grok-2-image-1212** không được công bố cụ thể trong thông tin có sẵn, nhưng dựa trên xu hướng của các mô hình **Grok-2** khác (như **Grok-2-vision-1212** và **Grok-2-1212**), nó có thể có giá tương tự: khoảng $2/1M token đầu vào và $10/1M token đầu ra. Tuy nhiên, vì đây là mô hình tạo hình ảnh, giá có thể được tính theo số lượng hình ảnh tạo ra thay vì token.
    

    + **Tuy nhiên, có một số điểm cần lưu ý:**

         1. Muốn tạo hình ảnh thì câu promt phải được bắt đầu bằng: "tạo hình ảnh ....." để gọi Model tạo hình ảnh **Grok-2-image-1212** xử lí tác vụ

              **VD:** tạo hình ảnh con mèo ,tạo hình ảnh anime cute girl, ....

        2. "Tạo hình ảnh cô gái anime với mắt đỏ" hoặc "Tạo hình ảnh cô gái anime tóc đỏ dễ thương" bị lỗi **"Error processing image: Error code: 400 - {'code': 'Client specified an invalid argument', 'error': 'Generated image rejected by content moderation'}"** vì Trong văn hóa anime, mắt đỏ thường được liên kết với các nhân vật phản diện, ma quỷ, hoặc có yếu tố bạo lực (ví dụ: nhân vật vampire, quỷ, hoặc trạng thái điên loạn). Hệ thống kiểm duyệt có thể tự động gắn cờ (flag) các đặc điểm như "mắt đỏ" vì lo ngại rằng hình ảnh có thể mang tính chất đáng sợ, bạo lực, hoặc không phù hợp.

        3. "Tạo hình ảnh cô gái anime tóc đỏ dễ thương" có vẻ vô hại, nhưng hệ thống kiểm duyệt có thể nhạy cảm với các yếu tố liên quan đến nhân vật anime nữ (thường dễ bị liên kết với nội dung nhạy cảm hoặc không phù hợp trong một số ngữ cảnh) nên có thể bị lỗi kiểm duyệt.

        4. "Tạo hình ảnh anime girl vampire tóc trắng dễ thương": Mặc dù có yếu tố "vampire", nhưng "tóc trắng" và "dễ thương" có thể làm giảm cảm giác đáng sợ. Hệ thống có thể hiểu đây là một nhân vật dễ thương, không mang tính bạo lực. Ngoài ra, "vampire" trong anime thường được mô tả theo cách lãng mạn hoặc dễ thương (như trong các bộ anime nổi tiếng), nên không bị gắn cờ.

    - **Do đó:**

        - Các từ như "mắt đỏ" hay "tóc đỏ" có thể bị gắn cờ vì liên quan đến bạo lực hoặc yếu tố đáng sợ. Ngay cả khi bạn không có ý định đó, hệ thống có thể diễn giải sai.

        - Sau khi hình ảnh được tạo, hệ thống kiểm tra các yếu tố như biểu cảm, trang phục, bối cảnh, và màu sắc. Nếu hình ảnh có bất kỳ yếu tố nào bị coi là không phù hợp (ví dụ: ánh mắt hung dữ, trang phục hở hang), nó sẽ bị từ chối.

        - "Tạo hình ảnh cô gái anime với mắt đỏ" hoặc "Tạo hình ảnh cô gái anime tóc đỏ dễ thương" bị lỗi là do hệ thống kiểm duyệt nội dung phát hiện các yếu tố tiềm ẩn nhạy cảm (như "mắt đỏ" liên quan đến bạo lực, hoặc nhân vật anime nữ dễ bị hiểu sai). Trong khi đó, các prompt như "tạo hình ảnh con mèo" hoặc "tạo hình ảnh anime girl vampire tóc trắng dễ thương" ít có khả năng vi phạm chính sách hơn, nên được chấp nhận.

    > Tôi gợi ý một prompt như: "Tạo hình ảnh cô gái anime tóc đỏ, mặc váy hoa, đứng trong công viên với ánh sáng dịu dàng và nụ cười vui vẻ". Prompt này có khả năng cao sẽ được chấp nhận vì nó định hướng rõ ràng theo hướng tích cực.

    ![img](/public/test_image.png)



### Cấu Trúc Thư Mục
```
├─ .chainlit
│  ├─ translations
│  │  ├─ bn.json
│  │  ├─ en-US.json
│  │  ├─ gu.json
│  │  ├─ he-IL.json
│  │  ├─ hi.json
│  │  ├─ ja.json
│  │  ├─ kn.json
│  │  ├─ ml.json
│  │  ├─ mr.json
│  │  ├─ nl-NL.json
│  │  ├─ ta.json
│  │  ├─ te.json
│  │  └─ zh-CN.json
│  └─ config.toml
├─ .files
│  └─ api
│     └─ main.py
├─ .env.example
├─ .gitignore
├─ chainlit.md
├─ grok_app.py
├─ requirements.txt
├─ triangle.png
└─ vercel.json

```


  **Have a fun conversation!** 💻😊



