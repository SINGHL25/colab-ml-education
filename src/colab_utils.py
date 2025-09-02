import os
import subprocess

def in_colab() -> bool:
    try:
        import google.colab  # type: ignore
        return True
    except ImportError:
        return False

def ensure_dirs():
    os.makedirs("results/logs", exist_ok=True)
    os.makedirs("results/plots", exist_ok=True)

def pip_install(packages):
    """Install packages inside Colab or local via pip."""
    cmd = ["pip", "install", "-q"] + list(packages)
    print("Installing:", " ".join(packages))
    subprocess.check_call(cmd)

def check_gpu():
    try:
        import torch
        return torch.cuda.is_available()
    except Exception:
        return False
