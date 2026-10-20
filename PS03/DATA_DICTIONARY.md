# Từ điển dữ liệu — PS03-AI
**Giảng viên: Nguyễn Bích Vân — IAI-UET-VNU**

## Phạm vi
Toàn bộ số liệu là **giả lập mới để dạy và học**, không phải dữ liệu cá nhân hoặc nhật ký sản phẩm thật. Không đổi tên dữ liệu OpenIntro rồi coi là dữ liệu AI. Mỗi bài có một bối cảnh riêng; không nối các CSV với nhau theo ID vì các ID chỉ duy nhất trong từng tệp. Dữ liệu của Bài 2–5 nằm trong bảng in ở đề, không cần CSV bên ngoài.

Các số dùng dấu chấm thập phân trong CSV. Ô trống là giá trị thiếu (NaN khi đọc bằng pandas), không phải số 0. Tên cột dùng **tiếng Anh dạng snake_case**; nhãn phân loại cũng được chuyển sang tiếng Anh. Số liệu, đơn vị và vị trí ô trống không đổi. Nhãn hình và giải thích vẫn có thể dùng tiếng Việt; `labs` không đổi tên cột. Ví dụ, `task="Summarization"` nghĩa là tác vụ tóm tắt văn bản. Tra các giá trị khác trong `VALUE_GLOSSARY_EN_VI.md`; dùng đúng nhãn khi lọc.

## Bài 1 — `exercise01_chatbot.csv` (12 dòng)
| Cột | Ý nghĩa |
|---|---|
| `id` | ID lượt thử, 1–12. |
| `task` | `FAQ`: hỏi đáp thường gặp; `Summarization`: tóm tắt; `Code`: hỗ trợ lập trình. |
| `input_tokens` | Số đơn vị văn bản đầu vào của lượt, số nguyên. Không đồng nhất một token với một từ. |
| `response_time_s` | Thời gian từ lúc gửi đến khi nhận đủ câu trả lời, giây. |
| `score` | Điểm chất lượng nguyên trên thang 0–10 theo tiêu chí giả định chung. |

## Bài 6 — `exercise06_responses.csv` (960 dòng)
Một dòng là một truy vấn. `id`: mã lượt; `task`: `FAQ` hoặc `Code explanation`; `response_time_s`: thời gian nhận đủ phản hồi, giây. Một số `response_time_s` thiếu. Khi so sánh phân phối, chỉ bỏ hàng thiếu các cột cần dùng và báo rõ số hàng bị bỏ theo tác vụ. Không áp dụng các ngưỡng 200 token/4 giây của Bài 1 cho tệp này.

## Bài 7 — `exercise07_annotations.csv` (420 dòng)
Một dòng là một phiên gán nhãn ảnh. `id`: mã phiên; `recording_method`: `Self-reported` hoặc `Stopwatch`; `duration_min`: số phút ghi lại, nguyên dương khi có dữ liệu. Cột này có ô trống. Hai cách ghi mô tả cách thu được thời lượng trong tình huống giả lập, không có cột thời gian chuẩn độc lập để đối chiếu. Không làm tròn thêm trước khi xét chữ số cuối.

## Bài 8 — `exercise08_ai_projects.csv` (240 dòng)
Một dòng là một sản phẩm AI nhỏ, không phải một sinh viên thật. `id`: mã sản phẩm; `evaluation_round`: đợt 1,2,3 dưới các nhãn `Round 1`, `Round 2`, `Round 3`. Các cột `quality_score`, `stability_score`, `presentation_score` là điểm thành phần trên thang 0–100. `total_score` bằng 0.5 chất lượng + 0.3 ổn định + 0.2 trình bày, làm tròn một chữ số thập phân trước khi mô phỏng mất một số ô khi trích xuất.

Có giá trị thiếu ở một số cột điểm. Khi vẽ một loại điểm, chỉ bỏ ô thiếu của loại điểm đó. Khi kiểm tra công thức tổng, chỉ dùng hàng có đủ bốn điểm. Không tự điền tổng điểm thiếu từ điểm thành phần trong bài yêu cầu mô tả tổng điểm đã ghi; làm như vậy sẽ đổi tập phân tích và phải được công bố riêng.

## Bài 9 — `exercise09_deployments.csv` (1.200 dòng)
Một dòng là một lượt **đã hoàn thành**. `id`: mã lượt; `configuration`: A/B; `input_length_group`: nhóm đầu vào đã được gắn nhãn `Short`, `Medium`, `Long` trong bộ thử; `response_time_s`: thời gian hoàn thành, giây. Không có cột số token chi tiết, thời gian của lượt không hoàn thành hoặc cơ chế phân công cấu hình. Không coi các lượt ở A/B là cặp đo trên cùng một đầu vào. Các biến dùng trong bài không thiếu. Thứ tự nhóm khi trình bày là ngắn → vừa → dài.

## Bài 10 — `exercise10_image_requests.csv` (1.000 dòng)
Một dòng là một yêu cầu **đã được tiếp nhận**, có kết quả cuối cùng:

| Cột | Ý nghĩa |
|---|---|
| `id` | Mã yêu cầu. |
| `concurrent_requests` | Số yêu cầu khác đang được xử lý khi yêu cầu này đến; số nguyên từ 0 đến 49. Đây không phải thời gian. |
| `processing_mode` | `Standard` hoặc `Economy`; nhãn chế độ trong nhật ký. |
| `failed` | 1 nếu không có ảnh hợp lệ trong 60 giây; 0 nếu có. Bao gồm timeout theo chính định nghĩa này. |

Tệp có cả thành công và thất bại, không thiếu các cột dùng trong bài. Dùng cùng biên `[0,10),…,[40,50)` cho tử số và mẫu số. Không vứt các lượt thành công trước khi đếm tổng số yêu cầu. Nếu một tổ hợp nhóm rỗng, tỉ lệ để NA, không điền 0%.

## Dữ liệu mẫu — `demo_drink_orders.csv` (24 dòng)
Một dòng là một đơn đồ uống sau seminar. `id`: mã đơn; `order_type`: `Takeaway`/`Dine-in`; `wait_time_min`: phút chờ; `item_count`: số món; `shift`: `Morning`/`Afternoon`. Tệp không thiếu giá trị. Chỉ dùng để học pandas/plotnine; các kết quả trên tệp này không trả lời Bài 6–10.

## Quy ước tính và tái lập
- SD dùng `ddof=1`; IQR = phân vị 0.75 trừ phân vị 0.25, nội suy tuyến tính.
- Biên histogram được nêu trong đề. Các bài Python đặt biên cuối lớn hơn mọi giá trị được vẽ; không làm mất quan sát ở biên cuối.
- Phần trăm là tỉ lệ nhân 100; mật độ phần trăm là phần trăm chia độ rộng khoảng. Nêu đúng đơn vị.
- Các tệp cố định đi kèm là cơ sở của đáp án. Không lấy một lần sinh ngẫu nhiên mới thay vào để đối chiếu với kết quả của bản này.


