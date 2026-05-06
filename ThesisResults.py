import matplotlib.pyplot as plt
import numpy as np

# 1. Define your 4 points (x, y)
x_values = np.array([4, 8, 16, 32])
y_values = np.array([264, 1322, 5089, 16952])

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Plot 1: Standard Linear Scale ---
ax1.plot(x_values, y_values, marker='o', linestyle='-', color='darkorange', label='Data Points')
ax1.set_title("Standard Linear Scale", fontsize=14)
ax1.set_xlabel("n (Input Size)", fontsize=12)
ax1.set_ylabel("Value", fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.legend()

# --- Plot 2: n log2 n Scale ---
# Use np.log2 for the transformation
n_log2_n = x_values * np.log2(x_values)

# Use raw strings r"..." to avoid SyntaxWarnings with LaTeX backslashes like \l
ax2.plot(n_log2_n, y_values, marker='s', linestyle='--', color='teal', label='Data Points')
ax2.set_title(r"$n \log_{2}(n)$ Transformed Scale", fontsize=14)
ax2.set_xlabel(r"$n \log_{2}(n)$ Transformation", fontsize=12)
ax2.set_ylabel("Value", fontsize=12)

# Set custom ticks to display original x_values on the transformed axis
ax2.set_xticks(n_log2_n)
ax2.set_xticklabels([str(val) for val in x_values])

ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.show()