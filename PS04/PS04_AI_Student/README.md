# PS04-AI — Tương quan và hồi quy trong dự án AI
**Nguyễn Bích Vân -IAI-UET-VNU**

## Bắt đầu
1. Giải nén. Mở thư mục chứa `data/` và `regression_tools.py` bằng File → Open Folder trong VS Code.
2. Mở `00_Regression_Template.ipynb`, chọn Select Kernel → Python Environments.
3. Nếu thiếu thư viện, chạy `%pip install -r requirements.txt` trong một ô notebook mới. Khởi động lại kernel.
4. Chạy mẫu trên `demo_drink_orders.csv`. Thay CONFIG để đổi tên CSV/cột/nhóm.
5. Làm tay Bài 1–6. Trong `PS04_AI_Student.ipynb`, bật RUN_LAB01/RUN_LAB02 khi bắt đầu thực hành Bài 7/Bài 9; điền phần nhận xét.

## Tệp chính
- PS04_AI_Exercises.pdf: đề sinh viên, 10 bài, 39 câu, không có đáp án.
- PS04_AI_Practice_Guide.pdf: hướng dẫn từng bước, 6 trang.
- 00_Regression_Template.ipynb: mẫu hoàn chỉnh, mặc định dùng một bộ dữ liệu học cú pháp riêng.
- PS04_AI_Student.ipynb: chỗ làm bài, mã hỗ trợ và ô viết nhận xét; không có đầu ra điền sẵn.
- regression_tools.py: các hàm dùng chung, không có đáp án riêng cho câu hỏi.
- regression_example.py: mẫu chạy cả file trong Terminal, in bảng và lưu ảnh.
- DATA_DICTIONARY.md: nghĩa tiếng Việt của các cột và đơn vị.
- data/: 7 CSV, tên tệp/cột/giá trị phân loại bằng tiếng Anh.


## Lưu ý
Tất cả số liệu là giả lập để học, không phải bằng chứng đánh giá một sản phẩm thật. Bài 6 cho sẵn hai phương trình để biến đổi đại số; không có CSV bắt buộc cho bài này.
Kết quả notebook hiện dưới ô, không ở Terminal. Bản script lưu hình vào `student_outputs/`. Các kết quả gần 0 như 1e-14 là sai số số học máy tính.
Không dùng thư viện của Python/Anaconda khác với kernel hiện tại. Không dán `PS ...>` hoặc `>>` vào ô mã.
