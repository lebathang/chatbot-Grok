# Chào mừng đến với chatbot Grok 🚀🤖

Xin chào mọi người 👋 Hôm nay mình share và hướng dẫn sử dụng con chatbot này, mặc dù còn đang phát triển nhưng tôi hy vọng mọi người sẽ thích và đóng góp nó 🥰

## Giới thiệu - Hướng dẫn 📖

- **API key:** trước tiên phải chuẩn bị api key Grok thì bạn phải vào [console.x.ai](https://console.x.ai/) để lấy API key 🔑	

- **Model xử lí văn bản (Language Models)":** Tôi sử dụng model **Grok-2-1212** cho xử lí các tác vụ liên quan đến văn bản, text. Đây là một mô hình ngôn ngữ (text-only) không có khả năng xử lý hình ảnh, tập trung vào việc tạo văn bản và trả lời các câu hỏi dựa trên văn bản, mô hình này được cải thiện về độ chính xác, khả năng tuân thủ hướng dẫn, và hỗ trợ đa ngôn ngữ so với phiên bản Grok-beta. Nó là phiên bản nâng cấp của Grok-beta, ra mắt cùng ngày 11/12/2024. 💬

    - Cung cấp câu trả lời chi tiết, rõ ràng cho các chủ đề phức tạp.
    - Có phong cách trò chuyện sáng tạo, phù hợp cho các dự án sáng tạo hoặc brainstorming.
    - Hỗ trợ đa ngôn ngữ tốt, phù hợp cho các ứng dụng toàn cầu.

    	+ **Dung lượng ngữ cảnh:** 128K token, lớn hơn nhiều so với **Grok-2-vision-1212 (hỗ trợ cả text và hình ảnh)**, phù hợp cho các cuộc hội thoại dài hoặc phân tích văn bản lớn.

        + **Giá cả:** có giá $2/1M token đầu vào và $10/1M token đầu ra, **Grok-2-vision-1212** cũng tương tự.

        ⇒ **Grok-2-1212** là lựa chọn tốt nhất xử lý văn bản và muốn dung lượng ngữ cảnh lớn, với hiệu suất tốt hơn **Grok-beta**

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

    
    **Have a fun conversation!** 💻😊
