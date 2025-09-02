
### `docs/gpu_tpu.md`
```markdown
# GPU / TPU
- Turn on GPU/TPU: `Runtime → Change runtime type`
- Check GPU:
```python
import torch; print(torch.cuda.is_available())
