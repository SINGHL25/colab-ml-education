# colab-ml-education
# Colab Learning Playground
<img width="427" height="438" alt="Screenshot 2025-09-02 231205" src="https://github.com/user-attachments/assets/59cd6838-7527-41f5-8940-3dd73b185433" />
<img width="2048" height="2048" alt="Gemini_Generated_Image_1sg7vn1sg7vn1sg7 (2)" src="https://github.com/user-attachments/assets/267a903d-650f-4010-bc7d-a0bd8484cb38" />



Hands-on repo to learn **Google Colab** from beginner → advanced:
- Setup & environment management
- Google Drive integration & data I/O
- GPU/TPU usage
- TensorFlow & PyTorch quick training runs
- Git/GitHub from Colab
- Testing (pytest) inside Colab notebooks
- Saving results (logs/plots) back to Drive or repo

## Quick Start (in Colab)
1. Open any notebook in `/notebooks`.
2. First run: execute the **Setup** cell to install dependencies.
3. For Drive access: run **Mount Drive** cell when prompted.

## Local Dev (optional)
```bash
git clone <your-repo-url>
cd colab-learning-playground
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
python main.py
```Plain text
colab-ml-education/
│── notebooks/
│    ├── 01_setup.ipynb
│    ├── 02_tensorflow.ipynb
│    └── 03_pytorch.ipynb
│
│── data/
│    └── sample.csv
│
│── tests/
│    └── test_sample.py
│
│── requirements.txt
│── README.md
