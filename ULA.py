import numpy as np
import matplotlib.pyplot as plt
import os

# Create results folder
os.makedirs("results", exist_ok=True)

# Parameters
M = 16              # number of antennas
d = 0.5             # spacing (in wavelengths)
wavelength = 1.0
k = 2 * np.pi / wavelength

# ULA antenna positions
antenna_positions = np.arange(M) * d

# Spatial grid (user positions)
x_positions = np.linspace(-5, 5, 200)
y_position = 5

# Channel model (LOS free-space)
def channel(x):
    distances = np.sqrt((antenna_positions - x)**2 + y_position**2)
    return np.exp(-1j * k * distances) / distances

# Generate example channel
h_sample = channel(0)

# Plot ULA geometry
plt.figure()
plt.scatter(antenna_positions, np.zeros_like(antenna_positions))
plt.title("Uniform Linear Array Geometry")
plt.xlabel("Antenna Position (λ)")
plt.ylabel("Array Axis")
plt.grid()
plt.savefig("results/ula_geometry.png")
plt.close()

print("ULA geometry figure saved.")
