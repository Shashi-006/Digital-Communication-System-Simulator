# Digital Communication System Simulator Using Python

## Project Overview

This mini project simulates a basic digital communication system using Python.

The current version implements:

- Random binary data generation
- BPSK modulation
- AWGN communication channel
- Coherent BPSK demodulation
- Bit Error Rate (BER) calculation
- BER vs SNR analysis
- Signal visualization using Matplotlib

## System Block Diagram

```text
Binary Data
     |
     v
BPSK Modulator
     |
     v
AWGN Channel
     |
     v
BPSK Demodulator
     |
     v
Recovered Data
     |
     v
BER Analysis
```

## Requirements

Python 3.x

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Open a terminal in this project folder and run:

```bash
python main.py
```

The program displays:

1. Original binary data
2. BPSK transmitted waveform
3. Received waveform after AWGN
4. BER vs SNR graph
5. Console results showing bit errors and BER

## Main Parameters

Open `main.py` and change:

```python
NUM_BITS = 100
SAMPLES_PER_BIT = 100
SNR_DB = 6
AMPLITUDE = 1.0
CARRIER_FREQUENCY = 5
```

## Project Flow

1. Generate random bits.
2. Convert bits into a BPSK waveform.
3. Add AWGN noise according to the selected SNR.
4. Demodulate the received waveform.
5. Compare transmitted and recovered bits.
6. Calculate BER.
7. Repeat the experiment for multiple SNR values.
8. Plot BER against SNR.

## Future Enhancements

The project can be extended with:

- ASK modulation
- FSK modulation
- QPSK modulation
- Constellation diagrams
- Eye diagrams
- GUI using Tkinter
- User-entered binary data
- CSV result export
- Comparison of BER for multiple modulation schemes

## Educational Purpose

This project is intended as an ECE mini project for understanding the basic operation of a digital communication system and the effect of channel noise on transmitted information.
