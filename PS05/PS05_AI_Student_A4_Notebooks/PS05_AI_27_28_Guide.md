# Hướng dẫn thực hành Bài 27–28 — PS05-AI

**Nguyễn Bích Vân — IAI-UET-VNU**

Tài liệu bổ sung cho bộ **PS05-AI, bản A4**. Nội dung đề bài và các lời giải A4 không bị thay đổi.

## 1. Mở tệp nào trước?

| Tệp | Người dùng | Nội dung |
|---|---|---|
| `00_Simulation_Template.ipynb` | Sinh viên và giảng viên | Hai ví dụ mẫu hoàn chỉnh, số liệu riêng; giải thích từng bước; chạy được ngay. |
| `PS05_AI_27_28_Student.ipynb` | Sinh viên | Đúng đề Bài 27–28; bốn vị trí cần tự điền trong hai ô cấu hình, mã xử lý phía sau đã chuẩn bị; chỗ viết lập luận. |

| `requirements.txt` | Cả hai | Danh sách thư viện cho phần notebook. |

Không cần CSV đầu vào. Các bài này sinh dữ liệu mô phỏng trực tiếp bằng NumPy. Các CSV trong thư mục kết quả chỉ xuất hiện **sau khi chạy**; không phải tệp bị thiếu trong gói tải về.

## 2. Chạy từng bước trong VS Code

1. Giải nén gói sinh viên hoặc giảng viên vào một thư mục riêng. Không mở notebook trực tiếp bên trong ZIP.
2. Chọn **File → Open Folder**, mở thư mục vừa giải nén.
3. Mở `00_Simulation_Template.ipynb`. Nếu chưa có, cài tiện ích **Python** và **Jupyter** của Microsoft trong VS Code.
4. Nhấn **Select Kernel** ở góc trên bên phải; chọn môi trường Python muốn dùng. Kernel là Python thực hiện các ô mã của notebook, có thể khác Python đang mở trong Terminal.
5. Chạy ô kiểm tra môi trường. Ô này in đường dẫn Python và các phiên bản thư viện.
6. Nếu báo thiếu thư viện, bỏ dấu `#` trước dòng `%pip install numpy pandas plotnine ipykernel`, chạy ô đó rồi **Restart Kernel**. Đây là lệnh chạy trong **ô code của notebook**, không phải lệnh PowerShell. Máy cần Internet cho lần cài thư viện.
7. Chạy các ô theo thứ tự bằng **Shift+Enter** hoặc nút ▶. Có thể dùng **Run All** để chạy toàn bộ notebook học mẫu.
8. Mở `PS05_AI_27_28_Student.ipynb`; đọc đề và điền lập luận trước khi chạy phần tương ứng.
9. Điền bốn vị trí `None` trong `CONFIG27` và `CONFIG28`, chạy lại các ô từ trên xuống. Sau khi đổi cấu hình nên dùng **Restart Kernel → Run All** để tránh dùng kết quả cũ.
10. Viết nhận xét vào các ô Markdown có chữ “Sinh viên điền”. Nhấn **Ctrl+S** để lưu cả mã, phần trả lời và kết quả.

**Kết quả nằm ngay dưới ô mã**, không phải Terminal. Hình có thể được xem ngay trong notebook; ô cuối còn lưu CSV/PNG vào đường dẫn đã in ra.

### Cài bằng Terminal khi cần

Dùng đúng Python đã chọn làm kernel. Ví dụ với đường dẫn Python 3.13 đã dùng trước đây:

```powershell
& "C:\Users\Pro 5\AppData\Local\Programs\Python\Python313\python.exe" -m pip install numpy pandas plotnine ipykernel
```

Chỉ dán phần bắt đầu từ `&`, không dán `PS D:\...>` hay `>>`. Nhấn **Enter**, không nhấn Shift+Enter. Sau khi cài, chọn lại đúng kernel và khởi động lại kernel.

## 3. Sinh viên phải sửa gì?

### Bài 27

Trong `CONFIG27`, tự điền:

| Mục | Việc cần quyết định |
|---|---|
| `high_exclusive` | Đầu phải của `integers`, để sinh đúng miền lựa chọn đề cho. |
| `sum_axis` | Chiều cộng, để có một tổng cho mỗi lượt thử. |

Có thể thay `seed` hoặc `n_trials` để thử nghiệm, nhưng giữ miền lựa chọn của đề khi nộp. Số lượt 100.000 là lựa chọn gợi ý cho mô phỏng, không phải yêu cầu mới bắt buộc.

Cần tự viết giải thích vì sao chọn đều các giá trị tổng có hoặc không tương đương với chọn hai giá trị rồi cộng. Mã chạy được không thay thế câu trả lời này.

### Bài 28

Trong `CONFIG28`, tự điền:

| Mục | Việc cần quyết định |
|---|---|
| `event_operator` | Một chuỗi trong `">"`, `">="`, `"<"`, `"<="`, `"=="`, đúng câu chữ biến cố. |
| `p_theory` | Xác suất đã tính bằng cách đếm trước khi mô phỏng. Có thể nhập một phân số Python. |

Ba cỡ mẫu của bài đã có sẵn. `seeds=[2026, 42]` giúp chạy hai lần để đối chiếu; có thể thêm seed khác. Không chọn bỏ các seed chỉ vì kết quả không khớp kỳ vọng.

## 4. Đọc các cột trong bảng kết quả

| Tên cột | Nghĩa tiếng Việt |
|---|---|
| `total_calls` | Tổng số lượt gọi công cụ của hai agent trong một lượt thử. |
| `count` | Số lượt có tổng tương ứng. |
| `seed` | Giá trị khởi tạo bộ sinh số giả ngẫu nhiên. |
| `n_trials` | Số lượt trong mẫu/tiền tố đang xét. |
| `event_count` | Số lượt thỏa biến cố. |
| `frequency` | Tần suất tương đối trong mẫu mô phỏng. |
| `theoretical_probability` | Xác suất suy ra từ mô hình của đề, không phải ước lượng bằng mô phỏng. |
| `absolute_error` | Giá trị tuyệt đối của tần suất trừ xác suất lý thuyết. |

Tên tệp, biến và cột đều bằng tiếng Anh; hướng dẫn và diễn giải bằng tiếng Việt.

## 5. Vì sao chạy bản sinh viên lúc đầu chưa có bảng?

Bản sinh viên **cố ý để trống bốn quyết định** ở các ô cấu hình. Khi còn `None`, chương trình in thông báo hướng dẫn, bỏ qua phần chưa hoàn thành và không tạo CSV rỗng. Đây không phải lỗi thư viện hay mất dữ liệu.

Notebook học mẫu không có các chỗ trống này, nên có thể chạy ngay để học cách viết mã. Mã mẫu có số liệu riêng, không chứa kết quả được điền sẵn cho hai bài cần nộp.

## 6. Những lỗi thường gặp

| Hiện tượng | Cách xử lý |
|---|---|
| `No module named 'plotnine'` hoặc `'numpy'` | Cài bằng `%pip` trong đúng notebook/kernel, rồi Restart Kernel. |
| `NameError` | Chưa chạy ô nhập thư viện hoặc ô tạo biến trước đó. Chạy lại từ đầu. |
| Có thông báo “hãy điền … None” | Điền đúng hai ô cấu hình, không xóa các dòng kiểm tra. |
| Kết quả có kích thước không mong muốn | In `.shape`; xem lại hàng, cột và chiều cộng. |
| CSV chưa xuất hiện | Chưa có bảng hợp lệ hoặc chưa chạy ô xuất kết quả ở cuối. |
| Không thấy PNG trong Explorer | Đọc đường dẫn tuyệt đối `OUTPUT_DIR` đã in; đó là nơi notebook ghi kết quả. |
| Muốn giữ kết quả nhiều lần chạy | Sao chép thư mục đầu ra trước khi chạy lại; tệp cùng tên được cập nhật. |

Không sửa tần suất bằng tay cho giống xác suất lý thuyết. Với cùng mô hình, tần suất là kết quả của lần mô phỏng; không phải mọi môi trường, seed hoặc cách gọi bộ sinh đều cho cùng một chuỗi.

## 7. Nộp gì?

Nộp `PS05_AI_27_28_Student.ipynb` đã lưu, có đủ mã đã hoàn thành, bảng/hình đầu ra và lập luận của sinh viên. Có thể kèm các CSV/PNG trong `ps05_27_28_outputs/student/` nếu giảng viên yêu cầu.

Không nộp riêng notebook học mẫu chưa chỉnh sửa thay cho bài làm. Không gửi bản giảng viên cho lớp trước hạn chữa bài.

## 8. Tài liệu tra cứu cú pháp

- NumPy `Generator.integers`: https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html
- NumPy `Generator.choice`: https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html
- plotnine `geom_col`: https://plotnine.org/reference/geom_col.html
- VS Code Jupyter Notebooks: https://code.visualstudio.com/docs/datascience/jupyter-notebooks
