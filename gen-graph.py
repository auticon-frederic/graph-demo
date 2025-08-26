#!/usr/bin/env python3

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4,  5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y, marker="o")

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Chart")

# Save as an image (PNG, JPG, SVG, etc.)
plt.savefig("chart.png")
