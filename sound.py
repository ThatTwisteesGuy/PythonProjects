import numpy as np
from scipy.io.wavfile import write

# =========================
# Signal Generators
# =========================

def sine_wave(freq, amp, duration, sample_rate=44100, duty_cycle=1.0):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    base = np.sin(2 * np.pi * freq * t)
    if duty_cycle < 1.0:
        period = 1 / freq
        phase = np.mod(t, period)
        mask = phase < (duty_cycle * period)
        base = base * mask
    return amp * base


def square_wave(freq, amp, duration, sample_rate=44100, duty_cycle=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    period = 1 / freq
    phase = np.mod(t, period)
    wave = np.where(phase < duty_cycle * period, 1.0, -1.0)
    return amp * wave


def line(gradient, intercept, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return gradient * t + intercept

# =========================
# Signal Operations
# =========================

def integrate(signal, sample_rate=44100):
    return np.cumsum(signal) / sample_rate


def multiply(signal1, signal2):
    return signal1 * signal2


def normalize(signal):
    max_val = np.max(np.abs(signal))
    if max_val == 0:
        return signal
    return signal / max_val


def save_wav(filename, signal, sample_rate=44100):
    signal = normalize(signal)
    signal_int16 = np.int16(signal * 32767)
    write(filename, sample_rate, signal_int16)

# =========================
# FM Function
# =========================

def frequency_modulate(carrier_freq, mod_signal, amp, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    phase = 2 * np.pi * (carrier_freq * t + integrate(mod_signal, sample_rate))
    return amp * np.sin(phase)

# =========================
# Main Script
# =========================

duration = 3.0
sr = 44100

# 1. Main audio (440 Hz square wave)
audio = sine_wave(freq=148, amp=0.5, duration=duration, sample_rate=sr, duty_cycle=0.1)

# 2. Generate triangle wave (via integrating square LFO)
lfo_square = square_wave(freq=3, amp=0.5, duration=duration, sample_rate=sr, duty_cycle=0.001)
triangle_lfo = integrate(lfo_square, sr)
triangle_lfo = normalize(triangle_lfo)

# 3. Convert to AM envelope (0 → 1)
am_envelope = (triangle_lfo + 1) / 2

# 4. Apply amplitude modulation
modulated = multiply(audio, am_envelope)

# 5. Save output
save_wav("am_triangle.wav", modulated, sr)

print("Saved am_triangle.wav")