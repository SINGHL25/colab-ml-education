
---

### `colab-learning-playground/main.py`
```python
"""
Optional local demo runner.
- Loads the sample CSV
- Produces a quick plot into ./results/plots/quick_plot.png
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    os.makedirs("results/plots", exist_ok=True)
    df = pd.read_csv("examples/data/sample.csv")
    print("Loaded sample.csv:")
    print(df.head())

    plt.figure()
    df.groupby("category")["value"].mean().plot(kind="bar", title="Mean value by category")
    out = "results/plots/quick_plot.png"
    plt.savefig(out, bbox_inches="tight")
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
