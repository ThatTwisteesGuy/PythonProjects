import numpy as np
from scipy.fft import fft


def analyze_vhdl_dft(in_re, in_im, vhdl_re, vhdl_im):
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


def display_results(input_re, input_im, vhdl_re_out, vhdl_im_out):
    results = analyze_vhdl_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

    print("-" * 30)
    print(f"SNR Calculation Results")
    print("-" * 30)
    print(f"SNR:  {results['snr_db']:.2f} dB")
    print("-" * 30)

    # Print Comparison
    print("Bin | Reference (SciPy) | VHDL (Actual)")
    for i in range(len(results['ref'])):
        print(f" {i}  | {results['ref'][i]:15.1f} | {results['actual'][i]:15.1f}")
