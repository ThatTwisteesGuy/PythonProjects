import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# Functions

def ss_value(y):
    return y[-1]


def settling_time(y):
    y_final = ss_value(y)
    y_settle = 0.95 * y_final

    # Find the first index where output crosses 10% and 90%
    t_settle = t[np.where(y >= y_settle)[0][0]]

    # Rise time
    return t_settle

def rise_time(y):
    y_final = ss_value(y)
    y10 = 0.1 * y_final
    y90 = 0.9 * y_final

    # Find the first index where output crosses 10% and 90%
    t10 = t[np.where(y >= y10)[0][0]]
    t90 = t[np.where(y >= y90)[0][0]]

    # Rise time
    return t90 - t10


def plotRL(G):
    fig, ax = plt.subplots()

    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.axhline(0, color='black', linewidth=1)  # Real axis
    ax.axvline(0, color='black', linewidth=1)  # Imag axis

    ctrl.root_locus(G, ax=ax)
    ax.set_aspect('auto')

    plt.show()

# Transfer Function of our System
s = ctrl.TransferFunction.s
G = 15 / ((s + 5) * (s + 1))


# RL Plot of KG(s) as K changes
plotRL(G)

# Values of K to perform analysis on
Gains = [0.1, 4/15 , 3]
Gains = [0.6, 3]

# Transient analysis
for K in Gains:
    # Open-loop system with gain
    G_open = K * G

    # Closed-loop system with unity feedback
    T = ctrl.feedback(G_open, 1)

    # Step response (unit amplitude)
    t, y = ctrl.step_response(T)

    # Scale to amplitude 5 to match 5V input step
    y_scaled = 5 * y

    # Plot
    plt.figure(figsize=(8,5))
    plt.plot(t, y_scaled, linewidth=2, color='blue')
    plt.title("Closed-Loop Step Response (Amplitude 5)")
    plt.xlabel("Time [s]")
    plt.ylabel("Output")
    plt.grid(True)
    plt.show()

    y_final = ss_value(y_scaled)
    y_peak = np.max(y_scaled)
    Mp_percent = ((y_peak - y_final) / y_final) * 100
    wn, zeta, _ = ctrl.damp(T, doprint=False)

    print("\n K = ", K)
    print("Rise time: ", rise_time(y_scaled))
    print("Settling time: ", settling_time(y_scaled))
    print("Steady State Value: ", ss_value(y_scaled))
    print("Peak: ", y_peak)
    print(f"Peak Overshoot: {Mp_percent:.2f}%")
    print("zeta: ", zeta, "wn: ",wn)