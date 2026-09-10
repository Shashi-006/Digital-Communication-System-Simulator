import numpy as np

def bpsk_modulate(bits, samples_per_bit=100, carrier_frequency=5, amplitude=1.0):
    """
    BPSK modulation:
    bit 1 -> phase 0
    bit 0 -> phase pi
    """
    t = np.arange(len(bits) * samples_per_bit) / samples_per_bit
    signal = np.zeros_like(t, dtype=float)

    for i, bit in enumerate(bits):
        start = i * samples_per_bit
        end = start + samples_per_bit
        local_t = t[start:end]
        phase = 0 if bit == 1 else np.pi
        signal[start:end] = amplitude * np.cos(
            2 * np.pi * carrier_frequency * local_t + phase
        )

    return signal, t
