#!/usr/bin/env python3

import matplotlib.pyplot as plt
import random

# Data
x = list(range(30))
y = list(map(lambda x: random.uniform(7,11), range(30)))

# Plot
plt.bar(x, y)
plt.ylim(bottom=0)
plt.savefig("chart.png")
