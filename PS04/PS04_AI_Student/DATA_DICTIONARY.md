# Từ điển dữ liệu PS04-AI
**Nguyễn Bích Vân -IAI-UET-VNU**

Tất cả là dữ liệu giả lập để học. Bảy CSV có đủ các giá trị cần dùng; không có ô thiếu. CSV gốc không chứa fitted/residual/đáp án; chúng được sinh ra khi phân tích.

| CSV | Một hàng / cột / đơn vị |
|---|---|
| exercise01_prompt_tuning.csv (5 hàng) | run_id: mã lượt; temperature: tham số sinh; quality_score: điểm chất lượng 0–100. |
| exercise02_response_time.csv (4 hàng) | request_id: mã yêu cầu; output_hundreds: trăm token đầu ra; response_time_s: giây; mode: Standard (thường), Accelerated (tăng tốc). Dùng Bài 2 và 4. |
| exercise03_execution_modes.csv (12 hàng) | request_id; input_hundreds: trăm token đầu vào; response_time_s: giây; mode: Standard/Accelerated. Bài 3 tính tay ở S03, S04, A01, A06 nhưng mô hình khớp trên 12 hàng. |
| exercise07_hardware_groups.csv (54 hàng) | request_id; environment: Edge (thiết bị biên), Workstation (máy trạm), Cloud (đám mây); output_tokens: một token, không phải trăm token; response_time_s: giây. Mỗi môi trường 18 hàng. |
| exercise08_team_summary.csv (12 hàng) | team_id: mã nhóm; retrieval_usage_pct: % yêu cầu dùng truy xuất; unsupported_answer_pct: % trả lời thiếu căn cứ. Đây là số tổng hợp giả lập ở cấp nhóm, không có bản ghi riêng từng yêu cầu. |
| exercise09_forward_reverse.csv (9 hàng) | request_id; output_hundreds: trăm token đầu ra; response_time_s: giây. Dùng so hai chiều hồi quy. |
| demo_drink_orders.csv (12 hàng) | order_id: mã đơn đồ uống; item_count: số món; wait_time_min: phút; service_mode: Standard (thường), Express (nhanh). Chỉ dùng học cú pháp. |

## Các tên trong bảng xử lý
x/y/group là bí danh các cột được cấu hình; fitted = giá trị khớp, residual = y - fitted, coefficient = hệ số, n = số hàng, SSE = tổng bình phương phần dư.
Tỉ lệ có hậu tố pct nằm trên thang 0–100. Chênh lệch hai phần trăm là điểm phần trăm.
Các CSV mô phỏng liên tục lưu hữu hạn chữ số. Không diễn giải mọi chữ số lưu trong CSV như độ chính xác của một phép đo thực tế.
