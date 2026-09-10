import numpy as np

def calculate_ber(original_bits, recovered_bits):
    """
    Calculate number of bit errors and BER.
    """
    n = min(len(original_bits), len(recovered_bits))

    errors = np.sum(original_bits[:n] != recovered_bits[:n])
    ber = errors / n if n else 0.0

    return int(errors), float(ber)
