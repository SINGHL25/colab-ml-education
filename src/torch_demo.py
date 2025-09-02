import torch
from torch import nn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

class MLP(nn.Module):
    def __init__(self, input_dim, classes):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 16),
            nn.ReLU(),
            nn.Linear(16, classes)
        )
    def forward(self, x):
        return self.net(x)

def train_iris(epochs=10, lr=1e-2, device=None):
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    X, y = load_iris(return_X_y=True)
    X = (X - X.mean(0)) / X.std(0)
    Xtr, Xte, Ytr, Yte = train_test_split(X, y, test_size=0.2, random_state=42)
    Xtr = torch.tensor(Xtr, dtype=torch.float32).to(device)
    Ytr = torch.tensor(Ytr, dtype=torch.long).to(device)
    Xte = torch.tensor(Xte, dtype=torch.float32).to(device)
    Yte = torch.tensor(Yte, dtype=torch.long).to(device)

    model = MLP(X.shape[1], len(np.unique(y))).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    model.train()
    for _ in range(epochs):
        opt.zero_grad()
        logits = model(Xtr)
        loss = criterion(logits, Ytr)
        loss.backward()
        opt.step()

    model.eval()
    with torch.no_grad():
        preds = model(Xte).argmax(dim=1)
        acc = (preds == Yte).float().mean().item()
    return model, acc
