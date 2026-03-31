# Signal Processing (Biomedical)

## Core Concepts
- Sampling theorem (Nyquist) — sample at 2x max frequency
- Fourier Transform — time → frequency domain
- Filtering — remove noise, isolate bands
- Convolution

## Filters
- **Butterworth** — maximally flat passband (used in EEG alpha filtering)
- Chebyshev — steeper rolloff, ripple
- FIR vs IIR tradeoffs
- `filtfilt` — zero-phase filtering (no time shift)

## Applied to Biosignals
| Signal | Key processing |
|--------|---------------|
| [[EEG]] | Bandpass 0.5–100Hz, ICA, epoching |
| ECG | R-peak detection, HRV |
| EMG | Envelope, RMS |
| fMRI | Hemodynamic response, GLM |

## Tools
- **Python:** scipy.signal, MNE
- **MATLAB:** Signal Processing Toolbox, EEGLAB

## Connects To
- [[EEG]]
- [[Biomedical-Engineering]]
- [[Python-Biomedical]]
- [[MRI]] (fMRI signal processing)

---
*Part of → [[HOME]] > [[Biomedical-Engineering]]*
