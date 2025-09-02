import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def plot_group_mean(df: pd.DataFrame, group_col: str, value_col: str, title: str, out_path: Optional[str] = None):
    plt.figure()
    df.groupby(group_col)[value_col].mean().plot(kind="bar", title=title)
    if out_path:
        plt.savefig(out_path, bbox_inches="tight")
    return plt.gcf()
