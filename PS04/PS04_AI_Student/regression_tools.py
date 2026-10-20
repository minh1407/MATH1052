"""Công cụ chung cho PS04-AI — Nguyễn Bích Vân -IAI-UET-VNU.
Không chứa đáp án riêng của bài tập. Chỉ đọc CSV local; không tải dữ liệu.
"""
from pathlib import Path
import re
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from plotnine import ggplot, aes, geom_point, geom_line, geom_abline, geom_hline, labs


def prepare_data(root, filename, x, y, group=None):
    """Chọn các hàng hợp lệ dùng chung cho những mô hình cần so sánh."""
    path = Path(root) / 'data' / filename
    if not path.is_file():
        raise FileNotFoundError(f'Không thấy {path}. Mở đúng thư mục chứa data/ hoặc sửa ROOT.')
    raw = pd.read_csv(path)
    required = [x, y] + ([group] if group else [])
    absent = [name for name in required if name not in raw.columns]
    if absent:
        raise ValueError(f'Thiếu cột {absent}. Các cột đang có: {list(raw.columns)}')
    data = pd.DataFrame({'x': pd.to_numeric(raw[x], errors='coerce'),
                         'y': pd.to_numeric(raw[y], errors='coerce')})
    data = data.replace([np.inf, -np.inf], np.nan)
    if group:
        data['group'] = raw[group].astype('string').str.strip().replace('', pd.NA)
    data = data.dropna().copy()
    if group:
        data['group'] = data['group'].astype(str)
    print(f'{filename}: ban đầu {len(raw)} hàng; giữ {len(data)}; loại {len(raw)-len(data)}.')
    print('Các hàng bị loại là thiếu/không hợp lệ ở đúng các cột đang dùng; không đổi thành 0.')
    if len(data) < 3:
        raise ValueError('Cần ít nhất 3 cặp hợp lệ để chạy mẫu thực hành này.')
    if data['x'].nunique() < 2 or data['y'].nunique() < 2:
        raise ValueError('Pearson r cần cả x và y có độ biến thiên khác 0.')
    return data.reset_index(drop=True)


def analyze(data, reference=None):
    """OLS có hệ số chặn; thêm biến nhóm khi có cột group."""
    simple = smf.ols('y ~ x', data=data).fit()
    reverse = smf.ols('x ~ y', data=data).fit()
    adjusted = None
    if 'group' in data:
        levels = sorted(data['group'].unique())
        reference = levels[0] if reference is None else reference
        if reference not in levels:
            raise ValueError(f'Mức tham chiếu {reference!r} không có trong {levels}.')
        formula = f'y ~ x + C(group, Treatment(reference={reference!r}))'
        adjusted = smf.ols(formula, data=data).fit()
        X = adjusted.model.exog
        if np.linalg.matrix_rank(X) < X.shape[1]:
            raise ValueError('Ma trận thiết kế thiếu hạng: chưa thể diễn giải hệ số duy nhất.')
    return {'data': data, 'r': data.x.corr(data.y), 'simple': simple,
            'reverse': reverse, 'adjusted': adjusted, 'reference': reference}


def numeric_summary(result):
    rows = []
    for label in ['simple', 'adjusted']:
        model = result[label]
        if model is not None:
            rows.append({'model': label, 'n': int(model.nobs),
                         'SSE': float(np.sum(model.resid**2)),
                         'sum_residuals': float(model.resid.sum()),
                         'sum_x_residuals': float(np.dot(result['data'].x, model.resid))})
    return pd.DataFrame(rows)


def make_plots(result, x_label='Biến giải thích x', y_label='Biến đáp ứng y'):
    d = result['data'].copy(); m = result['simple']; d['residual'] = m.resid
    mapping = aes('x', 'y', color='group') if 'group' in d else aes('x', 'y')
    plots = {
        'scatter_and_fit': (ggplot(d, mapping) + geom_point(size=2)
            + geom_abline(intercept=m.params['Intercept'], slope=m.params['x'])
            + labs(x=x_label, y=y_label, color='Nhóm', title='Quan sát và đường hồi quy gộp')),
        'residuals': (ggplot(d, aes('x', 'residual', color='group') if 'group' in d else aes('x', 'residual'))
            + geom_point(size=2) + geom_hline(yintercept=0, linetype='dashed')
            + labs(x=x_label, y='Phần dư (cùng đơn vị với y)', color='Nhóm', title='Phần dư của mô hình đơn'))}
    if result['adjusted'] is not None:
        grid = pd.concat([pd.DataFrame({'x': np.linspace(g.x.min(), g.x.max(), 50), 'group': name})
                          for name,g in d.groupby('group')], ignore_index=True)
        grid['fitted'] = result['adjusted'].predict(grid)
        plots['adjusted_fit'] = (ggplot(d, aes('x','y', color='group')) + geom_point(size=2)
            + geom_line(aes(y='fitted'),data=grid)
            + labs(x=x_label,y=y_label,color='Nhóm',title='Cùng hệ số góc; khác hệ số chặn theo nhóm'))
    return plots


def save_plots(plots, folder, prefix='practice'):
    folder = Path(folder); folder.mkdir(parents=True,exist_ok=True)
    prefix = re.sub(r'[^A-Za-z0-9_-]+', '_', str(prefix))
    paths=[]
    for name,p in plots.items():
        dest = folder / f'{prefix}_{name}.png'
        p.save(dest, width=7.2, height=4.4, dpi=140, verbose=False)
        paths.append(dest)
    return paths
