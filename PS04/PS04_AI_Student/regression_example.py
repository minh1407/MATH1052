"""Mẫu chạy từ Terminal — Nguyễn Bích Vân -IAI-UET-VNU.
Sửa CONFIG để thay dữ liệu; không chứa lời giải viết sẵn của bài tập.
"""
from pathlib import Path
import sys
try:
    from regression_tools import prepare_data, analyze, numeric_summary, make_plots, save_plots
except ImportError as exc:
    print('Không nạp được thư viện:',exc)
    print(f'& "{sys.executable}" -m pip install -r "{Path(__file__).with_name("requirements.txt")}"')
    raise SystemExit(1)

CONFIG = {'file':'demo_drink_orders.csv','x':'item_count','y':'wait_time_min',
          'group':'service_mode','reference':'Standard',
          'x_label':'Số món trong đơn','y_label':'Thời gian chờ (phút)'}

def main():
    root=Path(__file__).resolve().parent
    print('Python:',sys.executable)
    data=prepare_data(root,CONFIG['file'],CONFIG['x'],CONFIG['y'],CONFIG['group'])
    result=analyze(data,CONFIG['reference'])
    print('Pearson r:',result['r'])
    print('OLS đơn:\n',result['simple'].params)
    if result['adjusted'] is not None:
        print('OLS thêm nhóm:\n',result['adjusted'].params)
    print(numeric_summary(result).to_string(index=False))
    plots=make_plots(result,CONFIG['x_label'],CONFIG['y_label'])
    for path in save_plots(plots,root/'student_outputs','example'):
        print('Đã lưu:',path)
    print('HOÀN TẤT: kết quả trong Terminal; hình đã lưu ở student_outputs/.')

if __name__=='__main__':
    main()
