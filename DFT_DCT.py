import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt
from scipy.fft import dct

def analyse_vhdl_dft(in_re, in_im, vhdl_re, vhdl_im):
    """
    Compares VHDL DFT results against a SciPy reference.

    Parameters:
    in_re, in_im     : Lists/arrays of the input real/imag parts
    vhdl_re, vhdl_im : Lists/arrays of the VHDL output real/imag parts
    """

    scale_factor = 1/len(in_re)

    # 1. Convert separate parts into complex numpy arrays
    input_signal = np.array(in_re, dtype=float) + 1j * np.array(in_im, dtype=float)
    vhdl_results = np.array(vhdl_re, dtype=float) + 1j * np.array(vhdl_im, dtype=float)

    # 2. Compute Reference using SciPy
    # We apply the scale_factor to match the VHDL implementation's gain
    ref_dft = fft(input_signal) * scale_factor

    # 3. Compute Noise/Error
    error_signal = ref_dft - vhdl_results

    # 4. Compute Power
    sig_power = np.mean(np.abs(ref_dft) ** 2)
    noise_power = np.mean(np.abs(error_signal) ** 2)

    # 5. Compute SNR
    if noise_power < 1e-18:  # Effectively zero noise
        snr_db = float('inf')
    else:
        snr_db = 10 * np.log10(sig_power / noise_power)

    return {
        "snr_db": snr_db,
        "ref": ref_dft,
        "actual": vhdl_results
    }


def compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out):
    results = analyse_vhdl_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

    print("-" * 30)
    print(f"SNR Calculation Results")
    print("-" * 30)
    print(f"SNR:  {results['snr_db']:.2f} dB")
    print("-" * 30)

    # Print Comparison
    print("Bin | Reference (SciPy) | VHDL (Actual)")
    for i in range(len(results['ref'])):
        print(f" {i}  | {results['ref'][i]:15.1f} | {results['actual'][i]:15.1f}")



def analyse_vhdl_dct(input, vhdl_out):
    """
    Plots two arrays superimposed, plots their difference,
    and calculates/prints the Signal-to-Noise Ratio (SNR).
    """
    # Ensure inputs are numpy arrays
    signal = np.asarray(input)
    compared_signal = np.asarray(vhdl_out)

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


def compare_dct(input, vhdl_out):
    size = len(input)
    scipy_result = dct(input, norm=None, type=2) / (size * 2)
    analyse_vhdl_dct(scipy_result, vhdl_out)