# PS06-AI — Hướng dẫn thực hành
**Giảng viên: Nguyễn Bích Vân — IAI-UET-VNU**

## Mở và chạy trong VS Code
Giải nén gói vào một thư mục riêng. Chọn File → Open Folder để mở thư mục đó; mở `PS06_AI_Student.ipynb`, chọn kernel Python và chạy lần lượt các ô. Kết quả hiển thị ngay dưới ô mã. Trong một ô mới, có thể cài đúng kernel bằng `%pip install -r requirements.txt`, rồi Restart Kernel và Run All. Lệnh cài đặt chỉ chạy khi chủ động nhập vào ô, không cần chạy lại mỗi lần thực hành.

Notebook mẫu đã có một ví dụ hoàn chỉnh dùng tham số riêng. Các phần Bài 24–28 còn vị trí `None` để sinh viên tự chọn mô hình và điền tham số. Chưa điền thì chương trình chỉ nhắc và không tạo bảng rỗng. Bài 25 cần tự viết đoạn sinh chung một mảng rồi lấy hai tiền tố như đề yêu cầu; chạy hàm mẫu hai lần không thay thế yêu cầu này.

**Không cần CSV đầu vào.** Các thí nghiệm được mô phỏng trực tiếp. Bảng CSV và hình PNG chỉ là đầu ra, được tạo trong `student_outputs/` ; không được xem các mô phỏng là dữ liệu đo từ một hệ thống AI thật.

## Đọc mã theo ý nghĩa
- `np.arange(n+1)` tạo các số 0,…,n. Đầu phải của `arange` không được lấy.
- `samples.sum(axis=1)` cộng theo từng hàng; nếu một hàng là một lô, kết quả là một số đếm cho mỗi lô.
- `event.sum()` đếm số True; `event.mean()` là tần suất vì True=1, False=0.
- `np.bincount(..., minlength=...)` giữ các mức có tần số 0 trong miền cần vẽ.
- `geom_col()` dùng chiều cao có sẵn; `geom_point(aes(y="probability"))` có thể đặt điểm lý thuyết lên cùng trục.

## Chọn tham số SciPy
| Mô hình | Lệnh tạo | Ý nghĩa |
|---|---|---|
| Nhị thức | `stats.binom(n=..., p=...)` | n phép thử độc lập; cùng xác suất p |
| Siêu bội | `stats.hypergeom(M=..., n=..., N=...)` | M tổng thể; n phần tử loại cần đếm; N phần tử lấy không hoàn lại |
| Poisson | `stats.poisson(mu=...)` | mu ứng với trọn khoảng quan sát |

`dist.pmf(k)` là P(X=k), `dist.cdf(k)` là P(X≤k), `dist.sf(k)` là P(X>k). Khi X nguyên, P(X≥k)=`dist.sf(k-1)`. Khoảng a≤X≤b dùng `cdf(b)-cdf(a-1)` với a,b nguyên.

Trong mô phỏng nhị thức, số phép thử n khác số lần mô phỏng B. Trong siêu bội, loại gọi là “thành công” là loại đang đếm; có thể là nhãn lỗi. `replace=False` áp dụng bên trong từng gói; mỗi lần mô phỏng gói mới bắt đầu từ tổng thể ban đầu.

## Trước khi nộp
Ghi rõ biến cố, tham số và seed. Bảng phải có số lần, tần suất, lý thuyết, sai lệch; hình phải có tên trục. Nêu nhận xét bằng lời. Không khẳng định mô phỏng chứng minh công thức hay sai lệch buộc giảm sau mỗi lần tăng B. Với Poisson cắt miền vẽ, báo phần đuôi chưa vẽ, không chuẩn hóa lại PMF một cách tùy tiện.

## Tài liệu API đối chiếu
Các nguồn dưới đây chỉ để tra cứu cú pháp, không phải nguồn số liệu bài tập:
- SciPy binom: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html
- SciPy hypergeom: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hypergeom.html
- NumPy choice: https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html
- plotnine geom_col: https://plotnine.org/reference/geom_col.html
