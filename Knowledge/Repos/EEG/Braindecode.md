# Braindecode

**GitHub:** `braindecode/braindecode` | PyTorch-based

## What It Is
Deep learning framework for decoding raw EEG/MEG signals. Built on PyTorch + MNE. Feed Epochs directly into CNNs without reformatting.

## Key Architectures
- **EEGNet** — compact CNN, works with few channels/trials
- **Deep4Net** — deeper conv, better with more data
- **ShallowFBCSPNet** — hybrid filter-bank + CNN
- **EEGConformer** — Transformer-based

## Cropped Decoding
Key innovation: instead of one-label-per-trial, slides overlapping windows → more training samples, real-time BCI compatible.

## Data Augmentation (EEG-specific)
- Time-reverse, frequency shift, channel dropout
- Solves overfitting on small clinical datasets

## Install
```bash
pip install braindecode
```

## Quickstart
```python
from braindecode.models import EEGNetv4
model = EEGNetv4(n_chans=64, n_classes=4, input_window_samples=1000)
```

## Connects To
- [[MNE-Python]] — data source
- [[EEG]]
- [[MOABB]] — benchmark Braindecode models
- [[Signal-Processing]]

---
*Part of → [[Repos-Index]] > EEG*
