import matplotlib.pyplot as plt
import numpy as np

# --- Data Definition ---
# Define the two 2D arrays (lists of [x, y] coordinates).
# For a line plot, the order of the points matters, as they are connected sequentially.

# Dataset 1: Represents the first line (e.g., Temperature over time)
array1 = np.array([
    [1, 0],
    [2, 1],
    [3, 2],
    [4, 5],
    [5, 6],
    [6, 7],
    [8, 12],
    [12, 19],
    [16, 29],
    [18, 32],
    [21, 39],
    [24, 45]
])

# Dataset 2: Represents the second line (e.g., Humidity over time)
array2 = np.array([
    [1, 0],
    [2, 1],
    [3, 2],
    [4, 4],
    [5, 5],
    [6, 7],
    [8, 11],
    [12, 19],
    [16, 26],
    [18, 29],
    [21, 34],
    [24, 40]
])


# --- Data Preparation for Plotting ---
# We extract the X and Y coordinates for plotting.

# For Array 1
x1 = array1[:, 0]
y1 = array1[:, 1]

# For Array 2
x2 = array2[:, 0]
y2 = array2[:, 1]


# --- Plotting Configuration ---
plt.figure(figsize=(10, 6)) # Create a figure and set its size

# 1. Plot the first array as a line
plt.plot(
    x1, y1,
    color='blue',           # Line color
    linestyle='-',          # Solid line
    linewidth=2,            # Line thickness
    marker='o',             # Add markers at each data point
    label='Adder Trees'   # Label for the legend
)

# 2. Plot the second array as a line
plt.plot(
    x2, y2,
    color='red',            # Line color
    linestyle='--',         # Dashed line style
    linewidth=2,
    marker='s',             # Square markers
    label='Proposed Method'   # Label for the legend
)


# --- Customization and Labels ---
plt.title('Comparison of Addition Methods to Implement Hamming Weight (Line Graph)', fontsize=16)
plt.xlabel('Input Bits', fontsize=12)
plt.ylabel('Half Adders Required', fontsize=12)

# Display the legend to identify the lines
plt.legend(loc='upper left', frameon=True, shadow=True)

# Add a subtle grid
plt.grid(True, axis='y', linestyle=':', alpha=0.6)

# Improve visibility of axes limits
plt.xlim(array1[:, 0].min() - 0.5, array1[:, 0].max() + 0.5)
plt.ylim(0, 50) # Set Y limits from 0 to 12

# --- Display the Plot ---
plt.show()