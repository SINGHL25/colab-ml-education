from src.data_utils import load_csv, plot_group_mean
import os

def test_load_csv():
    df = load_csv("examples/data/sample.csv")
    assert not df.empty
    assert set(["id","category","value"]).issubset(df.columns)

def test_plot_group_mean(tmp_path):
    df = load_csv("examples/data/sample.csv")
    out = tmp_path / "plot.png"
    plot_group_mean(df, "category", "value", "mean by cat", str(out))
    assert out.exists()
