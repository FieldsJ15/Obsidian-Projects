# YASA — Yet Another Spindle Algorithm

**GitHub:** `raphaelvallat/yasa`

## What It Is
Best open-source Python tool for sleep EEG analysis. Auto sleep staging, spindle detection, slow-wave detection. Built on top of MNE.

## Performance (vs human raters)
| Stage | F1 Score |
|-------|---------|
| N1 | 87.0 ± 9.7 |
| N2 | 92.6 ± 9.7 |
| N3 | 83.9 ± 10.3 |
| REM | 78.5 ± 9.4 |

## Key Features
- Auto sleep staging (Wake, N1, N2, N3, REM) from 1–3 channels
- Spindle detection (sigma band, 12–15 Hz)
- Slow-wave detection (0.5–2 Hz)
- Spectral band power (delta, theta, alpha, sigma, beta)
- Artifact rejection

## Install
```bash
pip install yasa
```

## Quickstart
```python
import yasa
sls = yasa.SleepStaging(raw, eeg_name='C4-A1', eog_name='EOG', emg_name='EMG')
hypno = sls.predict()
yasa.plot_spectrogram(raw.get_data()[0], raw.info['sfreq'], hypno)
```

## Connects To
- [[MNE-Python]]
- [[EEG]]
- [[Signal-Processing]] (spindle = sigma band filtering)

---
*Part of → [[Repos-Index]] > EEG*
