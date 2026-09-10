# Digital Communication System Simulator

A Python-based digital communication system simulator that demonstrates **BPSK modulation, AWGN noise, coherent demodulation, and Bit Error Rate (BER) analysis**.

---

## 📌 Project Overview

Digital communication systems transmit information from a source to a receiver through a communication channel.

This project simulates a basic digital communication system using Python. The system generates random binary data, modulates it using **Binary Phase Shift Keying (BPSK)**, passes the signal through an **Additive White Gaussian Noise (AWGN)** channel, and then demodulates the received signal.

The recovered data is compared with the original transmitted data to calculate the **Bit Error Rate (BER)**.

---

## 🎯 Objectives

- Generate random binary data.
- Perform BPSK modulation.
- Simulate an AWGN communication channel.
- Perform coherent BPSK demodulation.
- Recover the transmitted binary data.
- Calculate the number of bit errors.
- Calculate Bit Error Rate (BER).
- Analyze BER for different Signal-to-Noise Ratio (SNR) values.
- Visualize transmitted and received signals using Python plots.

---

## ⚙️ Technologies Used

- **Python 3**
- **NumPy** – numerical computations and signal processing
- **Matplotlib** – signal visualization and plotting
- **Git & GitHub** – version control and project hosting

---

## 📡 System Block Diagram

```text
Random Binary Data
        │
        ▼
BPSK Modulation
        │
        ▼
Transmitted Signal
        │
        ▼
AWGN Channel
        │
        ▼
Received Signal
        │
        ▼
BPSK Demodulation
        │
        ▼
Recovered Binary Data
        │
        ▼
BER Calculation
        │
        ▼
Performance Analysis
