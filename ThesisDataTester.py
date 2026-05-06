import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct


def analyse_arrays(signal, compared_signal):
    """
    Plots two arrays superimposed, plots their difference,
    and calculates/prints the Signal-to-Noise Ratio (SNR).
    """
    # Ensure inputs are numpy arrays
    signal = np.asarray(signal)
    compared_signal = np.asarray(compared_signal)

    # Ensure they are the same length
    if len(signal) != len(compared_signal):
        raise ValueError("The two arrays must have the same length.")

    # Calculate the difference (Noise)
    noise = signal - compared_signal

    # --- Plotting ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # 1. Superimposed Graph
    ax1.plot(signal, label='Original Signal', color='blue', linewidth=2)
    ax1.plot(compared_signal, label='Compared Signal', color='orange', linestyle='--', linewidth=2)
    ax1.set_title('Superimposed Signals')
    ax1.set_xlabel('Sample Index')
    ax1.set_ylabel('Amplitude')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2. Difference Graph
    ax2.plot(noise, label='Difference (Signal - Compared)', color='red', linewidth=1.5)
    ax2.set_title('Difference Graph')
    ax2.set_xlabel('Sample Index')
    ax2.set_ylabel('Error / Difference Amplitude')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # --- SNR Calculation ---
    # Power is the mean of the squared amplitude
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)

    if noise_power == 0:
        print("SNR: Infinity (The arrays are perfectly identical)")
        return float('inf')

    snr_db = 10 * np.log10(signal_power / noise_power)

    # Print result
    print("-" * 30)
    print(f"Signal Power: {signal_power:.4f}")
    print(f"Noise Power:  {noise_power:.4f}")
    print(f"SNR:          {snr_db:.2f} dB")
    print("-" * 30)

    return snr_db


def compareDCT(input, VHDL_out):
    size = len(input)
    scipy_result = dct(input, norm=None, type=2) / (size * 2)
    analyse_arrays(scipy_result, VHDL_out)


# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":
    signal1 = np.array([
        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767,
        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767,
        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767,
        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767,
        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767,
        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767,
        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767,
        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767], dtype=float)

    signal2 = np.array([
        32767, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0], dtype=float)

    signal3 = np.array([
        32767, -32768, 32767, -32768, 32767, -32768, 32767, -32768,
        32767, -32768, 32767, -32768, 32767, -32768, 32767, -32768,
        32767, -32768, 32767, -32768, 32767, -32768, 32767, -32768,
        32767, -32768, 32767, -32768, 32767, -32768, 32767, -32768,
        32767, -32768, 32767, -32768, 32767, -32768, 32767, -32768,
        32767, -32768, 32767, -32768, 32767, -32768, 32767, -32768,
        32767, -32768, 32767, -32768, 32767, -32768, 32767, -32768,
        32767, -32768, 32767, -32768, 32767, -32768, 32767, -32768
    ], dtype=float)

    signal4 = np.array([32767, -32767, 32767, -32767, 32767, -32767, 32767, -32767,
                        32767, -32767, 32767, -32767, 32767, -32767, 32767, -32767,
                        32767, -32767, -32767, -32767, -32767, -32767, -32767, -32767,
                        -32767, -32767, -32767, -32767, -32767, -32767, -32767, 32767,
                        -32767, 32767, -32767, 32767, -32767, 32767, -32767, 32767,
                        -32767, 32767, -32767, 32767, -32767, 32767, -32767, 32767,
                        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767,
                        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767], dtype=float)

    VHDL_out1 = np.array(
        [32767, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)

    VHDL_out2 = np.array(
        [511, 511, 511, 510, 509, 508, 506, 504, 502, 499, 496, 493, 489, 486, 482, 477, 473, 468, 462, 457, 451, 445,
         439, 432, 425, 418, 411, 403, 395, 387, 379, 370, 362, 354, 344, 335, 325, 315, 305, 295, 285, 274, 264, 253,
         242, 231, 219, 208, 196, 185, 173, 161, 149, 137, 125, 113, 100, 88, 76, 63, 51, 38, 26, 13], dtype=float)

    VHDL_out3 = np.array(
        [-1, 512, 0, 513, 0, 515, 0, 519, 0, 524, 0, 531, 0, 539, 0, 548, 0, 560, 0, 573, 0, 588, 0, 605, 0, 626, 0,
         649, 0, 676, 0, 706, 0, 743, 0, 784, 0, 833, 0, 890, 0, 958, 0, 1039, 0, 1139, 0, 1264, 0, 1423, 0, 1633, 0,
         1920, 0, 2337, 0, 2995, 0, 4183, 0, 6960, 0, 20863], dtype=float)

    VHDL_out4 = np.array(
        [2047, -9806, 9873, 3248, 0, -1974, -3835, 2051, 2008, -505, 1392, 436, 0, -305, -1596, 1165, 1892, 35, 400,
         -172, 0, 422, -751, 804, 1702, 190, 64, -447, 0, 1017, -143, 542, 1448, 210, 8, -512, 0, 1613, 435, 301, 1138,
         140, 189, -329, 0, 2324, 1119, 38, 784, -28, 755, 353, 0, 3544, 2324, -355, 400, -460, 2844, 3484, 0, 9835,
         10895, -4346], dtype=float)

    compareDCT(signal1, VHDL_out1)
    compareDCT(signal2, VHDL_out2)
    compareDCT(signal3, VHDL_out3)
    compareDCT(signal4, VHDL_out4)

if __name__ == "__main__":
    signal1 = np.array([
        32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767], dtype=float)

    signal2 = np.array([
        32767, 0, 0, 0, 0, 0, 0, 0], dtype=float)

    signal3 = np.array([
        32767, -32768, 32767, -32768, 32767, -32768, 32767, -32768], dtype=float)

    signal4 = np.array([19280, -993, -29155, -6286, 20643, 16337, -4209, 1131], dtype=float)

    VHDL_out1 = np.array(
        [32767, 0, 0, 0, 0, 0, 0, 0], dtype=float)

    VHDL_out2 = np.array(
        [4095, 4017, 3784, 3405, 2896, 2276, 1568, 800], dtype=float)

    VHDL_out3 = np.array(
        [-1, 4175, 0, 4926, 0, 7373, 0, 20996], dtype=float)

    VHDL_out4 = np.array(
        [2093, -1257, 1063, 9255, 4665, -3042, -589, -1207], dtype=float)

    compareDCT(signal1, VHDL_out1)
    compareDCT(signal2, VHDL_out2)
    compareDCT(signal3, VHDL_out3)
    compareDCT(signal4, VHDL_out4)
