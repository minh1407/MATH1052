# PS05-AI — Tài liệu bài tập A4, biên dịch bằng pdfLaTeX

Tác giả đề: Nguyễn Bích Vân
Đơn vị: IAI-UET-VNU

Đây là tài liệu dạng article, không phải Beamer.
Có 28 bài, 89 câu hỏi; ba bài nâng cao là Bài 3, Bài 21 và Bài 23.
Các bối cảnh và số liệu là giả định phục vụ học tập.

## Biên dịch
Mở tệp .tex trong TeXstudio, chọn pdfLaTeX và biên dịch hai lần.
Mỗi tệp .tex chạy độc lập, không cần ảnh ngoài hoặc tệp LaTeX dùng chung.
Cần bộ gói LaTeX thông dụng: babel tiếng Việt, lmodern, TikZ, listings,
tcolorbox, geometry, hyperref, bookmark, enumitem, fancyhdr, lastpage.
Không dùng XeLaTeX, fontspec hoặc shell-escape.

## Nội dung
A: Bài 1–4, không gian mẫu và biến cố.
B: Bài 5–9, quy tắc tính xác suất.
C: Bài 10–15, xác suất có điều kiện.
D: Bài 16–20, độc lập.
E: Bài 21–25, toàn phần và Bayes.
F: Bài 26, tổng hợp theo quy trình.
G: Bài 27–28, mô phỏng Python.

Không cần CSV để làm bộ bài này: dữ kiện nằm trong đề;
hai bài Python sinh mẫu trực tiếp từ phép thử đã mô tả.

## Bản sinh viên
- PS05_AI_Exercises.tex: mã nguồn chỉ có đề bài.
- PS05_AI_Exercises.pdf: PDF 8 trang A4.
Không có đáp án hoặc mã giải của giảng viên trong gói sinh viên.


## Bổ sung notebook Bài 27–28

Mở `00_Simulation_Template.ipynb` để học trên ví dụ riêng, sau đó làm
`PS05_AI_27_28_Student.ipynb`. Bản sinh viên để bốn vị trí `None` trong
hai ô CONFIG; khi chưa điền, chương trình nhắc việc cần làm, không tạo CSV rỗng.
Hướng dẫn từng bước: `PS05_AI_27_28_Guide.md`.
Các notebook cần NumPy, pandas, plotnine và ipykernel; có `requirements.txt`.
Không cần dữ liệu đầu vào: hai bài tự sinh mẫu mô phỏng. Đề A4 không thay đổi.
