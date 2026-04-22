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

    signal4 = np.array([28551, 7947, 32270, 24996, 11390, 30115, -8550, 7289,
                        -13273, 32192, 3952, 10370, 24133, 22185, -29802, 14436,
                        19355, 23363, -32688, 14340, 1191, -29981, -26395, -21350,
                        -26455, 18632, 29125, 25787, 11742, -25824, -8385, -4349,
                        17950, 18248, -28613, -27344, 11196, -9712, 25604, -5731,
                        -22984, -30305, 15379, 28561, -29586, 15061, -20911, 9387,
                        26945, 2035, -3479, -27341, -22976, 21164, 9294, -23005,
                        -8068, 21891, 28402, 23018, 12988, 5964, -19218, 4528], dtype=float)

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
        [2885, 2219, 3810, 1065, 1685, -54, -557, -904, 1475, 3291, -7, 897, -3332, 1476, 815, 1216, -1634, -2415,
         -2118, 896, 1216, -49, -2971, 1017, 5525, -3833, 433, -93, -465, 494, 533, 2014, 74, 548, -2261, -2301, 173,
         -1852, 2561, 2731, 1644, -1484, 1320, -464, -1072, 2225, 596, -750, 300, -730, 3748, 1281, -732, 1723, 523,
         -1797, 1254, -207, -683, 1010, -602, -3016, -1861, -1388], dtype=float)

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

    signal4 = np.array([31779, -19535, -626, -5029, 31219, 13924, 1767, 12427], dtype=float)

    VHDL_out1 = np.array(
        [32767, 0, 0, 0, 0, 0, 0, 0], dtype=float)

    VHDL_out2 = np.array(
        [4095, 4017, 3784, 3405, 2896, 2276, 1568, 800], dtype=float)

    VHDL_out3 = np.array(
        [-1, 4175, 0, 4926, 0, 7373, 0, 20996], dtype=float)

    VHDL_out4 = np.array(
        [8240, -1736, 594, 6831, 6617, -166, 4450, 4883], dtype=float)

    compareDCT(signal1, VHDL_out1)
    compareDCT(signal2, VHDL_out2)
    compareDCT(signal3, VHDL_out3)
    compareDCT(signal4, VHDL_out4)
