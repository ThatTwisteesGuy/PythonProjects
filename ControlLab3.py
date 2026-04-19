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

def plotRL_with_points(G):
    # 1. Define the specific points to superimpose
    real_part = -10
    imag_part = 17.32

    # Define the two complex conjugate points
    s1 = complex(real_part, imag_part)  # -3 + j*sqrt(5)
    s2 = complex(real_part, -imag_part)  # -3 - j*sqrt(5)

    # 2. Setup the plot
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.axhline(0, color='black', linewidth=1)  # Real axis
    ax.axvline(0, color='black', linewidth=1)  # Imag axis

    # 3. Plot the Root Locus
    # Note: control.root_locus returns rlist, klist
    ctrl.root_locus(G, ax=ax, plot=True, xlim=[-32, 4], ylim=[-18, 18])

    # 4. Superimpose the desired points

    # Extract real and imaginary parts for plotting
    x_points = [s1.real, s2.real]
    y_points = [s1.imag, s2.imag]

    ax.plot(x_points, y_points,
            'o',  # Plot style: circles
            color='red',  # Color of the markers
            markersize=8,  # Size of the markers
            label='Target Closed-Loop Poles $s\'$'  # Label for the legend
            )

    # 5. Final Plot Configuration
    ax.set_aspect('equal', adjustable='box')  # Using 'equal' for better locus viewing
    ax.set_xlabel('Real Axis')
    ax.set_ylabel('Imaginary Axis')
    ax.set_title('Root Locus')

    plt.show()


gains = [0.714, 0.179]

for K in gains:

    s = ctrl.TransferFunction.s
    G = (K*218.75)/(s*(s+12.5))

    # RL Plot of KG(s) as K changes
    plotRL_with_points(G)

    # Open-loop system with gain
    G_open = G

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

    print("Rise time: ", rise_time(y_scaled))
    print("Settling time: ", settling_time(y_scaled))
    print("Steady State Value: ", ss_value(y_scaled))
    print("Peak: ", y_peak)
    print(f"Peak Overshoot: {Mp_percent:.2f}%")
    print("zeta: ", zeta, "wn: ",wn)


Td = 0.01876
Kp = 1.83

s = ctrl.TransferFunction.s
G = (Td*Kp*218.75)*(s+(1/Td))/(s*(s+12.5))

# RL Plot of KG(s) as K changes
plotRL_with_points(G)

# Open-loop system with gain
G_open = G

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

print("Rise time: ", rise_time(y_scaled))
print("Settling time: ", settling_time(y_scaled))
print("Steady State Value: ", ss_value(y_scaled))
print("Peak: ", y_peak)
print(f"Peak Overshoot: {Mp_percent:.2f}%")
print("zeta: ", zeta, "wn: ",wn)