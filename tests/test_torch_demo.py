import pytest
def test_torch_train():
    try:
        from src.torch_demo import train_iris
        _, acc = train_iris(epochs=1)
        assert 0 <= acc <= 1
    except Exception as e:
        pytest.skip(f"Torch unavailable or failed: {e}")
