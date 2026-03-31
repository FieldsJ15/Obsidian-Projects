# MOABB — Mother of All BCI Benchmarks

**GitHub:** `NeuroTechX/moabb`

## What It Is
Standardized benchmarking for BCI algorithms. Fixes the reproducibility crisis in EEG — everyone was comparing against poorly-tuned baselines. MOABB forces fair comparisons.

## What It Provides
- 30+ public EEG datasets auto-downloaded
- Paradigms: Motor Imagery, P300, SSVEP
- Standardized preprocessing pipelines
- Statistical comparison framework (Bayesian, permutation tests)
- CodeCarbon: tracks energy/CO2 of your pipeline

## Key Finding
Riemannian geometry pipelines beat deep learning when data is small. DL only wins with many subjects/trials.

## Install
```bash
pip install moabb
```

## Use Case
```python
from moabb.datasets import BNCI2014001
from moabb.paradigms import MotorImagery
dataset = BNCI2014001()
paradigm = MotorImagery()
X, y, metadata = paradigm.get_data(dataset)
```

## Connects To
- [[MNE-Python]]
- [[Braindecode]]
- [[EEG]]

---
*Part of → [[Repos-Index]] > EEG*
