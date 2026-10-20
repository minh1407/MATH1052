# Bắt đầu với PS03-AI
**Nguyễn Bích Vân • IAI-UET-VNU • UET.MAT1052**

## Tệp nên mở trước
1. Đọc `PS03_AI_Exercises.pdf` (10 bài, 54 câu).
2. Giải nén toàn bộ gói. Trong VS Code chọn **File → Open Folder**, mở thư mục có các notebook và `data/`.
3. Mở `00_Learn_Plotnine.ipynb`, chọn **Select Kernel**, chọn Python. Hình và bảng hiện ngay dưới ô mã.
4. Nếu thiếu thư viện, tạo một ô Code và chạy `%pip install -r requirements.txt`; sau đó Restart Kernel. Không dán `PS ...>` hoặc `>>` vào ô Python. Có cả Anaconda và Python 3.13 thì kiểm tra `sys.executable` ở ô đầu.
5. Chạy notebook mẫu từ trên xuống, rồi mở `PS03_AI_Student.ipynb`. TODO là phần bạn cần tự viết; khung chạy hết chưa có nghĩa đã làm xong bài.

`PS03_AI_Plotnine_Guide.pdf` giải thích từng đoạn mẫu. `DATA_DICTIONARY.md` nói rõ đơn vị quan sát, ý nghĩa cột và ô thiếu. Dữ liệu đã nằm trong `data/`, không cần tải lại.

## Có phải dữ liệu thật không?
Không. Đây là các bộ dữ liệu giả lập mới, được thiết kế riêng cho bài học; không phải đánh giá sản phẩm hoặc con người thật. Hãy phân biệt kết luận từ tệp bài tập với một khẳng định ngoài đời.

## Dùng tệp `.py` thay notebook
`plotnine_examples.py` dùng cùng mẫu cú pháp, chỉ đọc `demo_drink_orders.csv`. Chạy bằng **Run Python File in Terminal**; các bảng hiện ở Terminal, các hình PNG lưu ở `example_script_figures/`. Tệp không giải Bài 6–10. Notebook có thuận lợi là nhìn hình ngay dưới từng đoạn mã.
## Trước khi nộp
Bài 1–5 làm tay. Bài 6–10 cần mã, kết quả và nhận xét bằng lời. Restart Kernel → Run All rồi lưu notebook. Báo rõ mẫu số, đơn vị, biên chia và tập quan sát sau khi bỏ thiếu. Không đổi tên hoặc sửa CSV chỉ để làm cho kết quả khớp một nhận xét định sẵn.

