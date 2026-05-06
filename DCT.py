import numpy as np
from scipy.fft import dct


def true_half_packed_dct(x):
    N = len(x)
    assert N % 2 == 0, "Signal length N must be even for N/2 packing."

    # 1. REORDER AND PACK into z[n] of size N/2
    # First, conceptually reorder x[n] into a sequence y[n] where:
    # y = [even indices of x] + [reversed odd indices of x]
    y = np.concatenate([x[::2], x[1::2][::-1]])

    # Pack the even indices of 'y' into the Real part,
    # and the odd indices of 'y' into the Imaginary part.
    z = y[::2] + 1j * y[1::2]

    print(z)

    # 2. N/2 POINT FFT
    Z = np.fft.fft(z) / 32

    print(Z)

    # 3 & 4. POST-PROCESSING (Untangle and Twiddle)
    k = np.arange(N)

    # We need to access Z with modulo arithmetic because the N-point
    # reconstruction requires wrapping around the N/2-point FFT data.
    k_mod = k % (N // 2)
    k_rev = (N // 2 - k_mod) % (N // 2)

    # Grab Z[k] and Z^*[-k]
    Z_k = Z[k_mod]
    Z_k_rev_conj = np.conj(Z[k_rev])

    # Extract the separate FFTs of the real and imaginary parts
    # (This recovers the transform of y[::2] and y[1::2])
    Z_even = (Z_k + Z_k_rev_conj)
    Z_odd = -1.0j * (Z_k - Z_k_rev_conj)


    A = Z_even * np.exp(-1j * 2 * np.pi * k / (4*N))
    B = Z_odd * np.exp(-1j * 2 * np.pi * 5 * k / (4*N))

    Y = A+B

    X_dct = np.real(Y)

    return X_dct


# --- Verification Side-by-Side ---
##signal = np.array([2145, -3102,   980,  1455, -2890,   304, -1201,  3802,-1554,  2765,  -499,  3110, -3450,   812,  1920, -2250])
##signal = np.array([3200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
##signal = np.array([4096, -1234, 18204, -32000, 85, -9999, 2210, -512])
##signal = np.array([4096, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
signal = np.array([4096, -1234,  18204, -32000,     85,  -9999,   2210,   -512,
           42, -5555,  12345, -12345,   7777,  -8888,    999,  -1111,
        25000, -4000,    123,   -321,  31000, -31000,     15,    -15,
         8192, -8192,   4096,  -4096,   2048,  -2048,   1024,  -1024,
       4096, -1234, 18204, -32000, 85, -9999, 2210, -512,
       42, -5555, 12345, -12345, 7777, -8888, 999, -1111,
       25000, -4000, 123, -321, 31000, -31000, 15, -15,
       8192, -8192, 4096, -4096, 2048, -2048, 1024, -1024
                   ])


my_packed_res = true_half_packed_dct(signal) / 1
scipy_res = dct(signal, norm=None, type=2) / 32

print(f"{'Index':<8} | {'N/2 Packed DCT':<18} | {'SciPy DCT':<18} | {'Diff'}")
print("-" * 65)
for i in range(len(signal)):
    diff = abs(my_packed_res[i] - scipy_res[i])
    print(f"{i:<8} | {my_packed_res[i]:<18.6f} | {scipy_res[i]:<18.6f} | {diff:<10.2e}")

print(f"\nExact Match: {np.allclose(my_packed_res, scipy_res)}")

