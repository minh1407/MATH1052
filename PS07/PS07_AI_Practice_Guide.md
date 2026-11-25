# Hướng dẫn thực hành PS07-AI — Bài 15
**Giảng viên: Nguyễn Bích Vân — IAI-UET-VNU**

## 1. Mở đúng môi trường
Giải nén gói, mở cả thư mục trong VS Code rồi mở `PS07_AI_Student.ipynb`. Chọn **Select Kernel** và đúng Python đang sử dụng. Kết quả xuất hiện ngay dưới ô mã, không phải trong Terminal.

Nếu thiếu thư viện, chạy trong một ô notebook:
```python
%pip install -r requirements.txt
```
Khởi động lại kernel sau khi cài, rồi chạy các ô từ đầu. `%pip` cài vào môi trường của kernel đang chạy; tránh nhầm với Python trong Anaconda hoặc một bản Python khác trên máy. Các phiên bản trong `requirements.txt` là môi trường đã thử, không phải khẳng định chúng là phiên bản mới nhất.

## 2. Học mẫu rồi điền dữ kiện
Ví dụ đầu dùng một hộp riêng để giải thích mảng và trục; đó không phải dữ liệu của Bài 15. Trong `CONFIG_BOX`, điền danh sách 12 thẻ từ Bài 6, lựa chọn `axis` và `ddof`. Trong `CONFIG_CLT`, điền kỳ vọng và SD cá thể của phân phối mũ.

Khi còn `None`, notebook sẽ nhắc phần thiếu và không tạo bảng CSV rỗng. Sau khi điền đúng, chạy **Restart Kernel and Run All**. Dữ liệu được mô phỏng trực tiếp, nên không có thư mục CSV đầu vào.

## 3. Đọc mã theo ý nghĩa
`rng.choice` chọn các vị trí trong hộp; thẻ có giá trị trùng vẫn là những thẻ riêng. `size=(B,n)` tạo B lô, mỗi lô n quan sát. `sum` và `mean` phải tổng hợp đúng trục để mỗi lô có một kết quả. `rng.exponential(scale=...)` nhận thang đo, không phải tham số tốc độ.

Trong plotnine, `ggplot(data,aes(...))` chọn dữ liệu và ánh xạ; `geom_density` ước lượng đường mật độ từng nhóm khi ánh xạ màu theo nhóm. Đối với CLT, `after_stat("density")` đổi trục dọc histogram sang mật độ để so sánh với `norm.pdf`. `inherit_aes=False` giúp lớp đường tham chiếu dùng đúng các cột trong bảng riêng.

## 4. Các tệp nộp
Nộp lời giải viết tay Bài 1–14 và 16-17; notebook đã chạy cho Bài 15; các bảng và hai hình trong `student_outputs/`. Giữ tên tệp, tên cột bằng tiếng Anh, diễn giải bằng tiếng Việt. Không chỉ nộp ảnh chụp màn hình. Bảng `box_summary.csv` gồm cỡ mẫu, trung bình/SD thực nghiệm và lý thuyết của tổng và trung bình; các cột có hậu tố `empirical` là mô phỏng, `theory` là lý thuyết.


