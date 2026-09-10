import numpy as np
import matplotlib.pyplot as plt

from modulation import bpsk_modulate
from demodulation import bpsk_demodulate
from channel import add_awgn
from analysis import calculate_ber


# ============================================================
# DIGITAL COMMUNICATION SYSTEM SIMULATOR
# Version 2 - BPSK + AWGN + Demodulation + BER
# ============================================================

# -----------------------------
# SYSTEM PARAMETERS
# -----------------------------

NUM_BITS = 100
SAMPLES_PER_BIT = 100
SNR_DB = 6
AMPLITUDE = 1.0
CARRIER_FREQUENCY = 5


# ============================================================
# 1. GENERATE RANDOM BINARY DATA
# ============================================================

np.random.seed(42)

bits = np.random.randint(0, 2, NUM_BITS)

print("\n" + "=" * 60)
print("       DIGITAL COMMUNICATION SYSTEM SIMULATOR")
print("=" * 60)

print("\nOriginal Binary Data:")
print("".join(map(str, bits)))


# ============================================================
# 2. BPSK MODULATION
# ============================================================

tx_signal, time = bpsk_modulate(
    bits,
    samples_per_bit=SAMPLES_PER_BIT,
    carrier_frequency=CARRIER_FREQUENCY,
    amplitude=AMPLITUDE
)


# ============================================================
# 3. AWGN CHANNEL
# ============================================================

rx_signal = add_awgn(
    tx_signal,
    SNR_DB
)


# ============================================================
# 4. BPSK DEMODULATION
# ============================================================

recovered_bits = bpsk_demodulate(
    rx_signal,
    samples_per_bit=SAMPLES_PER_BIT,
    carrier_frequency=CARRIER_FREQUENCY
)


# ============================================================
# 5. BER CALCULATION
# ============================================================

errors, ber = calculate_ber(
    bits,
    recovered_bits
)


# ============================================================
# 6. DISPLAY RESULTS
# ============================================================

print("\n" + "-" * 60)

print("Communication Results")

print("-" * 60)

print(f"Number of Bits       : {NUM_BITS}")
print(f"SNR                  : {SNR_DB} dB")
print(f"Bit Errors           : {errors}")
print(f"Bit Error Rate (BER) : {ber:.6f}")

print("\nRecovered Binary Data:")
print("".join(map(str, recovered_bits)))

print("\n" + "=" * 60)


# ============================================================
# 7. DISPLAY FIRST 20 BITS
# ============================================================

display_bits = 20

original_display = bits[:display_bits]
recovered_display = recovered_bits[:display_bits]


print("\nFirst 20 Bits Comparison:")
print("-" * 60)

print("Original :  ", " ".join(map(str, original_display)))
print("Received :  ", " ".join(map(str, recovered_display)))

print("-" * 60)


# ============================================================
# 8. PLOT COMMUNICATION SIGNALS
# ============================================================

display_samples = display_bits * SAMPLES_PER_BIT

plt.figure(figsize=(14, 12))


# ------------------------------------------------------------
# ORIGINAL BINARY DATA
# ------------------------------------------------------------

plt.subplot(4, 1, 1)

bit_time = np.arange(display_bits)

plt.step(
    bit_time,
    original_display,
    where="post"
)

plt.title("Original Binary Data")
plt.xlabel("Bit Number")
plt.ylabel("Bit")

plt.ylim(-0.2, 1.2)
plt.grid(True)


# ------------------------------------------------------------
# BPSK TRANSMITTED SIGNAL
# ------------------------------------------------------------

plt.subplot(4, 1, 2)

plt.plot(
    time[:display_samples],
    tx_signal[:display_samples]
)

plt.title("BPSK Transmitted Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.grid(True)


# ------------------------------------------------------------
# RECEIVED SIGNAL WITH AWGN
# ------------------------------------------------------------

plt.subplot(4, 1, 3)

plt.plot(
    time[:display_samples],
    rx_signal[:display_samples]
)

plt.title(
    f"Received Signal with AWGN (SNR = {SNR_DB} dB)"
)

plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.grid(True)


# ------------------------------------------------------------
# RECOVERED BINARY DATA
# ------------------------------------------------------------

plt.subplot(4, 1, 4)

plt.step(
    bit_time,
    recovered_display,
    where="post"
)

plt.title(
    f"Recovered Binary Data | Bit Errors = {errors} | BER = {ber:.4f}"
)

plt.xlabel("Bit Number")
plt.ylabel("Bit")

plt.ylim(-0.2, 1.2)
plt.grid(True)


plt.tight_layout()

plt.show()


# ============================================================
# 9. BER VS SNR ANALYSIS
# ============================================================

snr_values = np.arange(0, 13, 2)

ber_values = []


for snr in snr_values:

    # Generate BPSK signal
    tx, _ = bpsk_modulate(
        bits,
        samples_per_bit=SAMPLES_PER_BIT,
        carrier_frequency=CARRIER_FREQUENCY,
        amplitude=AMPLITUDE
    )

    # Add AWGN
    rx = add_awgn(
        tx,
        snr
    )

    # Demodulation
    recovered = bpsk_demodulate(
        rx,
        samples_per_bit=SAMPLES_PER_BIT,
        carrier_frequency=CARRIER_FREQUENCY
    )

    # BER
    _, test_ber = calculate_ber(
        bits,
        recovered
    )

    ber_values.append(test_ber)


# ============================================================
# 10. DISPLAY BER TABLE
# ============================================================

print("\n")
print("=" * 40)
print("         BER vs SNR RESULTS")
print("=" * 40)

print("SNR (dB)        BER")
print("-" * 40)

for snr, ber_result in zip(snr_values, ber_values):

    print(
        f"{snr:>5}          {ber_result:.6f}"
    )

print("=" * 40)


# ============================================================
# 11. BER VS SNR GRAPH
# ============================================================

plt.figure(figsize=(9, 6))

plt.semilogy(
    snr_values,
    np.maximum(ber_values, 1e-6),
    marker="o"
)

plt.title("BER vs SNR for BPSK")

plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")

plt.grid(
    True,
    which="both"
)

plt.xticks(snr_values)

plt.show()