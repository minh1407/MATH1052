"""Mã mẫu học plotnine 
Chỉ dùng demo_drink_orders.csv, không giải sẵn Bài 6--10.
Chạy tệp .py sẽ in bảng và lưu hình ở example_script_figures/.
"""
from pathlib import Path
N_PLOT = 0

def display(obj):
    global N_PLOT
    if hasattr(obj, "save") and hasattr(obj, "draw"):
        N_PLOT += 1
        folder = Path(__file__).resolve().parent / "example_script_figures"
        folder.mkdir(exist_ok=True)
        dest = folder / f"example_{N_PLOT:02d}.png"
        obj.save(dest, width=7.6, height=4.5, dpi=140, verbose=False)
        print("Da luu hinh:", dest)
    else:
        print(obj.to_string(index=False) if hasattr(obj, "to_string") else obj)

import sys
print(sys.executable)

from pathlib import Path
import numpy as np
import pandas as pd

from plotnine import (
    ggplot, aes, geom_point, geom_histogram, after_stat,
    geom_rect, geom_bar, geom_col, geom_hline,
    geom_boxplot, geom_line, facet_wrap, labs, scale_x_continuous
)

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
demo = pd.read_csv(DATA / "demo_drink_orders.csv")
display(demo.head())
print("So dong, so cot:", demo.shape)
print(demo.dtypes)
print(demo.isna().sum())

x = demo.dropna(subset=["order_type", "wait_time_min"]).copy()
print("So dong bi bo:", len(demo) - len(x))

p = (
    ggplot(demo, aes(x="item_count", y="wait_time_min", color="order_type"))
    + geom_point(size=2, alpha=0.7)
    + labs(x="So mon trong don", y="Thoi gian cho (phut)",
           color="Kieu don", title="Mot don la mot diem")
)
display(p)

OUT = ROOT / "example_figures"
OUT.mkdir(exist_ok=True)
p.save(OUT / "scatter.png", width=7, height=4, dpi=150)
p.save(OUT / "scatter.pdf", width=7, height=4)

chon = demo.query("item_count >= 2 and wait_time_min < 8").copy()
chon["long_wait"] = chon["wait_time_min"] >= 6
bang = (
    chon.groupby("order_type", observed=True)
    .agg(n=("id", "size"),
         n_long_wait=("long_wait", "sum"),
         long_wait_rate=("long_wait", "mean"))
    .reset_index()
)
bang["percent"] = 100 * bang["long_wait_rate"]
display(bang)

chon = demo.loc[
    (demo["item_count"] >= 2) & (demo["wait_time_min"] < 8)
].copy()

edges = [0, 2, 4, 6, 8, 10, 12]
p_count = (
    ggplot(demo, aes(x="wait_time_min"))
    + geom_histogram(breaks=edges, closed="left")
    + labs(x="Thoi gian cho (phut)", y="So don")
)
display(p_count)

p_density = (
    ggplot(demo, aes(x="wait_time_min", y=after_stat("100*density")))
    + geom_histogram(breaks=edges, closed="left")
    + facet_wrap("~ order_type", scales="fixed")
    + labs(x="Thoi gian cho (phut)", y="Mat do (% / phut)")
)
display(p_density)

edges = np.array([0, 3, 5, 9, 12])
values = demo["wait_time_min"].dropna().to_numpy()
counts, _ = np.histogram(values, bins=edges)
assert counts.sum() == len(values)

bins = pd.DataFrame({
    "bin_left": edges[:-1], "bin_right": edges[1:], "n": counts
})
bins["percent"] = 100 * bins["n"] / len(values)
bins["percent_density"] = bins["percent"] / (bins["bin_right"] - bins["bin_left"])
display(bins)
print("Tong dien tich:",
      (bins["percent_density"] * (bins["bin_right"] - bins["bin_left"])).sum())

p = (
    ggplot(bins, aes(xmin="bin_left", xmax="bin_right",
                     ymin=0, ymax="percent_density"))
    + geom_rect()
    + scale_x_continuous(breaks=edges.tolist())
    + labs(x="Thoi gian cho (phut)", y="Mat do (% / phut)")
)
display(p)

bang = (
    demo.groupby("order_type", observed=True)
    .agg(n=("id", "size"),
         n_long_wait=("wait_time_min", lambda s: (s >= 6).sum()))
    .reset_index()
)
bang["percent"] = 100 * bang["n_long_wait"] / bang["n"]
p = (ggplot(bang, aes(x="order_type", y="percent"))
     + geom_col()
     + labs(x="Kieu don", y="Ti le cho it nhat 6 phut (%)"))
display(p)

digit = demo["wait_time_min"].astype(int) % 10
freq = digit.value_counts().reindex(range(10), fill_value=0)
bang_digit = pd.DataFrame({"last_digit": range(10), "n": freq.to_numpy()})
bang_digit["percent"] = 100 * bang_digit["n"] / len(digit)
p = (ggplot(bang_digit, aes(x="last_digit", y="percent"))
     + geom_col() + geom_hline(yintercept=10, linetype="dashed")
     + scale_x_continuous(breaks=list(range(10))))
display(p)

x = demo.copy()
x["wait_bin"] = pd.cut(
    x["wait_time_min"], bins=[0, 3, 6, 9, 12], right=False
)
assert x["wait_bin"].notna().all()
bang = (x.groupby("wait_bin", observed=False)
        .agg(n=("id", "size")).reset_index())
bang["wait_bin"] = bang["wait_bin"].astype(str)
display(bang)

thu = pd.DataFrame({
    "id": [1, 2, 3], "trial_1": [4.2, 5.1, 3.8],
    "trial_2": [3.9, 5.4, 4.0], "trial_3": [4.0, 5.0, 3.6]
})
dai = thu.melt(id_vars="id", value_vars=["trial_1", "trial_2", "trial_3"],
               var_name="trial", value_name="time_s")
display(dai)
p = (ggplot(dai, aes(x="trial", y="time_s", group="id"))
     + geom_point() + geom_line()
     + labs(x="Lan do", y="Thoi gian (giay)"))
display(p)
print("HOAN TAT: ma mau da chay het.")
