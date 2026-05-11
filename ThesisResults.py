import matplotlib.pyplot as plt

# Data from the table
bit_widths = [16, 18, 20]

# SNR values for each test case
test_data = {
    "DIRAC": [70.58, 74.6, 74.6],
    "NYQUIST": [85.01, 85.01, 85.01],
    "COSINE": [81.66, 78.9, 78.9],
    "RANDOM": [77.88, 79.53, 79.53],
    "RANDOM2": [79.25, 77.66, 77.66],
    "RANDOM3": [81.5, 81.5, 81.5]
}

plt.figure(figsize=(10, 6))

# Plot each line
for test_name, snr_values in test_data.items():
    plt.plot(bit_widths, snr_values, marker='o', label=test_name, linewidth=2)

# Formatting the chart
plt.title("8-DCT Accuracy (SNR vs. Bit-Width)", fontsize=14)
plt.xlabel("W", fontsize=12)
plt.ylabel("SNR (dB)", fontsize=12)
plt.xticks(bit_widths)  # Ensure only 16, 18, 20 show on X-axis
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title="Test Cases", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()


# Data from the table
bit_widths = [16, 17, 18, 19, 20]

# SNR values for each test case (excluding DC)
test_data = {
    "DIRAC":   [53.43, 54.89, 55.78, 56.04, 56.48],
    "NYQUIST": [76.67, 76.91, 77.05, 77.23, 77.24],
    "COSINE":  [73.33, 74.43, 74.33, 74.45, 74.52],
    "RANDOM":  [67.48, 67.85, 67.85, 67.98, 68.20],
    "RANDOM2": [67.45, 68.58, 68.53, 68.94, 69.00],
    "RANDOM3": [68.47, 68.36, 69.21, 69.04, 69.24]
}

plt.figure(figsize=(11, 7))

# Plot each line with a unique color/marker
for test_name, snr_values in test_data.items():
    plt.plot(bit_widths, snr_values, marker='s', label=test_name, linewidth=2, markersize=6)

# Formatting the chart
plt.title("64-DCT SNR Performance vs. W", fontsize=14, fontweight='bold')
plt.xlabel("W", fontsize=12)
plt.ylabel("Signal-to-Noise Ratio (dB)", fontsize=12)
plt.xticks(bit_widths)
plt.grid(True, which='both', linestyle='--', alpha=0.5)

# Adding a legend outside the plot area
plt.legend(title="Test Cases", bbox_to_anchor=(1.05, 1), loc='upper left', frameon=True)

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

# Data from the table
# Categories represent different N-point sizes and internal factorizations
dft_configs = ["4-DFT", "8-DFT", "16-DFT(4_4)", "16-DFT(8_2)", "32-DFT(8_4)", "32-DFT(16_2)"]

test_data = {
    "DIRAC":   [80.77, 73.41, 66.79, 66.79, 60.48, 60.48],
    "RANDOM1": [85.17, 81.34, 79.04, 77.00, 74.26, 72.52],
    "RANDOM2": [85.96, 80.77, 77.54, 74.21, 73.63, 71.73],
    "RANDOM3": [82.36, 81.04, 78.34, 74.96, 73.93, 72.54]
}

plt.figure(figsize=(12, 7))

# Plot each test case
for test_name, snr_values in test_data.items():
    plt.plot(dft_configs, snr_values, marker='D', label=test_name, linewidth=2, markersize=8)

# Formatting
plt.title("SNR Degradation vs. DFT Size and Architecture", fontsize=14, fontweight='bold')
plt.xlabel("DFT Configuration (N-Points and Factorisation)", fontsize=12)
plt.ylabel("SNR (dB)", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(rotation=15) # Rotate labels slightly for readability


plt.legend(title="Test Cases", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

dft_types = [
    "4-DFT",
    "8-DFT",
    "16-DFT(4_4)",
    "16-DFT(8_2)",
    "32-DFT(8_4)",
    "32-DFT(16_2)"
]

clks = [1, 6, 7, 11, 12, 16]

# Create the plot
plt.figure(figsize=(10, 6))
bars = plt.bar(dft_types, clks, color='#5dade2', edgecolor='#2e4053', linewidth=1.2)

# Customizing the appearance
plt.title('Latency: Clock Cycles per DFT Type', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('DFT Configuration', fontsize=12, fontweight='bold')
plt.ylabel('Number of Clock Cycles (CLKS)', fontsize=12, fontweight='bold')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding the exact values on top of each bar for clarity
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.3, yval, ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data from the tables
dft_types = ["4-DFT", "8-DFT", "16-DFT(4_4)", "16-DFT(8_2)", "32-DFT(8_4)", "32-DFT(16_2)"]
f_max = [491.1591, 260.1457, 231.5887, 242.5418, 226.5519, 234.7418]

# Create the first plot (Bar Graph)
plt.figure(figsize=(10, 6))
plt.bar(dft_types, f_max, color='#3498db', edgecolor='#2c3e50')

# Adding labels and title
plt.title('Maximum Frequency ($f_{max}$) vs. DFT Type', fontsize=14, fontweight='bold', pad=15)
plt.ylabel('Frequency (MHz)', fontsize=12, fontweight='bold')
plt.xlabel('DFT Configuration', fontsize=12, fontweight='bold')
plt.xticks(rotation=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add exact values on top of bars
for i, v in enumerate(f_max):
    plt.text(i, v + 5, f"{v:.1f}", ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data from the tables
dft_types = ["4-DFT", "8-DFT", "16-DFT(4_4)", "16-DFT(8_2)", "32-DFT(8_4)", "32-DFT(16_2)"]
luts = [264, 1394, 4817, 5366, 15859, 17850]
ffs = [264, 2268, 6512, 9004, 22480, 28516]

# Create the second plot (Line Graph)
plt.figure(figsize=(10, 6))
plt.plot(dft_types, luts, marker='o', markersize=8, label='LUTs', color='#e67e22', linewidth=2)
plt.plot(dft_types, ffs, marker='s', markersize=8, label='FFs', color='#27ae60', linewidth=2)

# Adding labels and title
plt.title('FPGA Resource Utilisation: LUTs vs. Flip-Flops', fontsize=14, fontweight='bold', pad=15)
plt.ylabel('Resource Count', fontsize=12, fontweight='bold')
plt.xlabel('DFT Configuration', fontsize=12, fontweight='bold')
plt.xticks(rotation=20)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Adding labels for exact counts
for i, v in enumerate(luts):
    plt.text(i, v + 500, str(v), ha='right', color='#e67e22', fontsize=9, fontweight='bold')
for i, v in enumerate(ffs):
    plt.text(i, v + 500, str(v), ha='left', color='#27ae60', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Specific radix-2 data points
n_vals = np.array([4, 8, 16, 32])
labels = ["4-DFT", "8-DFT", "16-DFT(8_2)", "32-DFT(16_2)"]

# Resource counts from your synthesis data
luts = np.array([264, 1394, 5366, 17850])
ffs = np.array([264, 2268, 9004, 28516])

# Calculate the n log n values (Base 2)
# n=4  -> 4*2 = 8
# n=8  -> 8*3 = 24
# n=16 -> 16*4 = 64
# n=32 -> 32*5 = 160
x_scale = n_vals * np.log2(n_vals)

plt.figure(figsize=(10, 6))

# Plotting against n log n scale
plt.plot(x_scale, luts, marker='o', markersize=8, label='LUTs', color='#d35400', linewidth=2.5)
plt.plot(x_scale, ffs, marker='s', markersize=8, label='Flip-Flops', color='#218c74', linewidth=2.5)

# Formatting the chart
plt.title('FPGA Resource Scaling on $n log_2 n$ Scale', fontsize=14, fontweight='bold')
plt.xlabel('DFT Type and Configuration', fontsize=12, fontweight='bold')
plt.ylabel('Hardware Resource Count', fontsize=12, fontweight='bold')
plt.xticks(x_scale, labels) # Map the n log n points to their respective DFT names
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Adding data labels for exact counts
for i in range(len(x_scale)):
    plt.text(x_scale[i], luts[i] + 500, str(luts[i]), ha='center', color='#d35400', weight='bold')
    plt.text(x_scale[i], ffs[i] - 1500, str(ffs[i]), ha='center', color='#218c74', weight='bold')

plt.tight_layout()
plt.show()

w_labels = ["W=16", "W=18", "W=20"]
f_max_w = [232.40, 217.82, 217.72]

plt.figure(figsize=(8, 6))
plt.bar(w_labels, f_max_w, color='#9b59b6', width=0.5)
plt.title('Max Frequency Implemented for 8-DCT vs ($W$)', fontweight='bold')
plt.ylabel('Frequency (MHz)')
plt.ylim(min(f_max_w) - 5, max(f_max_w) + 5)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

bit_widths = ["W = 16", "W = 17", "W = 18", "W = 19"]
f_max_values = [214.5923, 218.9621, 207.8138, 214.9613]

plt.figure(figsize=(8, 6))
bars = plt.bar(bit_widths, f_max_values, color='skyblue', edgecolor='navy')

# Add labels and title
plt.xlabel('Bit Width (W)', fontweight='bold')
plt.ylabel('Maximum Frequency (f_max) [MHz]', fontweight='bold')
plt.title('f_max vs. W', fontweight='bold')

# Adjust y-axis limit to show differences more clearly
plt.ylim(min(f_max_values) - 5, max(f_max_values) + 5)

# Add value labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 4), ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data for 8-DCT resource utilization across different bit widths (W)
w_values = [16, 18, 20]
lut_counts = [3200, 3453, 3533]
ff_counts = [4414, 4790, 4824]

plt.figure(figsize=(10, 6))

# Plotting LUTs
plt.plot(w_values, lut_counts, marker='o', linestyle='-', color='#e67e22', linewidth=2.5, label='LUTs')

# Plotting FFs
plt.plot(w_values, ff_counts, marker='s', linestyle='-', color='#27ae60', linewidth=2.5, label='FFs')

# Adding Titles and Labels
plt.title('8-DCT Resource Utilisation vs. Bit Width ($W$)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Internal Bit Width ($W$)', fontsize=12, fontweight='bold')
plt.ylabel('Resource Count', fontsize=12, fontweight='bold')

# Setting specific x-ticks and grid
plt.xticks(w_values)
plt.grid(True, linestyle='--', alpha=0.6)

# Adding value labels for clarity
for i, txt in enumerate(lut_counts):
    plt.annotate(f'{txt}', (w_values[i], lut_counts[i]), textcoords="offset points",
                 xytext=(0, 10), ha='center', color='#d35400', weight='bold')

for i, txt in enumerate(ff_counts):
    plt.annotate(f'{txt}', (w_values[i], ff_counts[i]), textcoords="offset points",
                 xytext=(0, 10), ha='center', color='#1e8449', weight='bold')

plt.legend()
plt.tight_layout()
plt.show()

# Data for 64-DCT resource utilization across different bit widths (W)
# Extracted from image_f7a741.png
w_values = [16, 17, 18, 19]
lut_counts = [47811, 49863, 51971, 54322]
ff_counts = [64173, 67038, 69913, 73168]

plt.figure(figsize=(10, 6))

# Plotting LUTs and FFs on the same line graph
plt.plot(w_values, lut_counts, marker='o', linestyle='-', color='#e67e22', linewidth=2.5, label='LUTs')
plt.plot(w_values, ff_counts, marker='s', linestyle='-', color='#27ae60', linewidth=2.5, label='FFs')

# Adding Titles and Labels
plt.title('64-DCT Resource Utilisation vs. Bit Width ($W$)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Internal Bit Width ($W$)', fontsize=12, fontweight='bold')
plt.ylabel('Resource Count', fontsize=12, fontweight='bold')

# Setting specific x-ticks and grid
plt.xticks(w_values)
plt.grid(True, linestyle='--', alpha=0.6)

# Adding value labels for clarity
for i, txt in enumerate(lut_counts):
    plt.annotate(f'{txt}', (w_values[i], lut_counts[i]), textcoords="offset points",
                 xytext=(0, 10), ha='center', color='#d35400', weight='bold')

for i, txt in enumerate(ff_counts):
    plt.annotate(f'{txt}', (w_values[i], ff_counts[i]), textcoords="offset points",
                 xytext=(0, 10), ha='center', color='#1e8449', weight='bold')

plt.legend()
plt.tight_layout()
plt.show()