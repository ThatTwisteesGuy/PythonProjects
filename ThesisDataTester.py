import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct


def analyze_arrays(signal, compared_signal):
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


# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":

    signal = np.array([15000, -22000,    314,     -8,  16384, -16384,   5050,   -123,
             0,  32767, -32768,     55,    -99,   8888,  -7777,    444,
           200,   -200,  10000, -15000,    256,   -512,   1024,  -2048,
          1234,   5678,  -9101,   1112,   1314,  -1516,   1718,  -1920,
           111,   -222,    333,   -444,    555,   -666,    777,   -888,
           999,  -1000,   2000,  -3000,   4000,  -5000,   6000,  -7000,
          8000,  -9000,  10000, -11000,  12000, -13000,  14000, -15000,
         16000, -17000,  18000, -19000,  20000, -21000,  22000, -23000])

    scipy_res = dct(signal, norm=None, type=2) / 64

    VHDL_out = np.array([-610,285,-149,676,-255,262,-581,97,-690,88,-662,43,-740,169,-229,1062,547,1139,-229,91,-800,267,-648,-268,-1411,-70,-6,1948,1849,3410,2565,2837,391,334,-844,834,140,1215,-227,1533,1494,3693,1851,1912,-946,42,-1884,-579,-2554,287,-899,1458,-1050,2315,1150,6135,2540,4609,-1626,2797,-5485,4199,-6039,2814], dtype=float)

    print(scipy_res)
    print(VHDL_out)

    analyze_arrays(scipy_res, VHDL_out)