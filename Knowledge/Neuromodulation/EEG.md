# EEG — Electroencephalography

## Physics
- Measures summed postsynaptic potentials from cortical pyramidal neurons
- Electrodes on scalp — high temporal resolution (ms), low spatial (~cm)
- Standard: 10-20 system (19–256 channels)

## Frequency Bands
| Band | Hz | State |
|------|-----|-------|
| Delta | 0.5–4 | Deep sleep |
| Theta | 4–8 | Drowsy, memory |
| **Alpha** | **8–13** | **Relaxed, eyes closed** |
| Beta | 13–30 | Active thinking |
| Gamma | 30–100+ | Cognitive processing |

> Alpha band (8–13 Hz) — already worked on with Butterworth filter, canal 79

## Key Techniques
- **ERPs** — Event-Related Potentials (P300, N200, N400)
- **ERSP** — Event-Related Spectral Perturbation
- **Coherence** — connectivity between regions
- **ICA** — artifact removal (eye blinks, muscle)

## Software
- **MNE-Python** — main open-source EEG analysis library
- EEGLAB (MATLAB)
- Brainstorm
- FieldTrip

## Connects To
- [[TMS]] (TMS-EEG — gold standard for cortical excitability)
- [[tDCS]] (measure effects of stimulation)
- [[Signal-Processing]]
- [[Neuromodulation]]
- [[MRI]] (EEG-fMRI simultaneous)

---
*Part of → [[HOME]] > [[Neuromodulation]]*
