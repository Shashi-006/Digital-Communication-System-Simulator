import numpy as np

def bpsk_demodulate(received_signal, samples_per_bit=100, carrier_frequency=5):
    """
    Coherent BPSK demodulation using correlation with the carrier.
    """
    recovered_bits = []

    for start in range(0, len(received_signal), samples_per_bit):
        end = start + samples_per_bit
        segment = received_signal[start:end]

        if len(segment) < samples_per_bit:
            break

        local_t = np.arange(samples_per_bit) / samples_per_bit
        carrier = np.cos(2 * np.pi * carrier_frequency * local_t)

        correlation = np.sum(segment * carrier)

        recovered_bits.append(1 if correlation >= 0 else 0)

    return np.array(recovered_bits, dtype=int)
