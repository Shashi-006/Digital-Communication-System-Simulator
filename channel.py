import numpy as np

def add_awgn(signal, snr_db):
    """
    Additive White Gaussian Noise channel.
    SNR is specified in dB.
    """
    signal_power = np.mean(signal ** 2)
    snr_linear = 10 ** (snr_db / 10)
    noise_power = signal_power / snr_linear
    noise_std = np.sqrt(noise_power)

    noise = np.random.normal(0, noise_std, len(signal))
    return signal + noise
