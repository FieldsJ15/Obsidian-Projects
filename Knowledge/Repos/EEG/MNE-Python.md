# MNE-Python

**GitHub:** `mne-tools/mne-python` | 5K+ stars | BSD License

## What It Is
The gold standard for EEG/MEG/fNIRS analysis in Python. Object-oriented: Raw → Epochs → Evoked pipeline. Replaces MATLAB EEGLAB for automated, reproducible pipelines.

## Core Objects
| Object | What it holds |
|--------|-------------|
| `Raw` | Continuous recording |
| `Epochs` | Segmented trials around events |
| `Evoked` | Averaged ERP |
| `SourceEstimate` | Cortical source activity |

## Key Features
- Bandpass filtering, ICA artifact removal
- Source localization (minimum norm, LCMV beamformer)
- Time-frequency analysis (Morlet wavelets, multitaper)
- Connectivity analysis
- Native fNIRS support
- MRI co-registration (Nibabel integration)

## Install
```bash
pip install mne
```

## Quickstart
```python
import mne
raw = mne.io.read_raw_edf('your_file.edf', preload=True)
raw.filter(1, 40)  # bandpass
raw.plot()
```

## Connects To
- [[EEG]] — primary framework
- [[Signal-Processing]] — filtering, ICA
- [[Braindecode]] — feeds Epochs directly into DL models
- [[MOABB]] — benchmark pipelines built on MNE
- [[YASA]] — sleep analysis on top of MNE

---
*Part of → [[Repos-Index]] > EEG*
