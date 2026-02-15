import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import os

os.makedirs("results", exist_ok=True)

M = 16
d = 0.5
wavelength = 1.0
k = 2 * np.pi / wavelength

antenna_positions = np.arange(M) * d
y_position = 5

def channel(x):
    distances = np.sqrt((antenna_positions - x)**2 + y_position**2)
    return np.exp(-1j * k * distances) / distances

# Spatial grid
x_positions = np.linspace(-5, 5, 300)

# Generate manifold
H = np.array([channel(x) for x in x_positions])

# Stack real and imaginary parts
H_real = np.hstack([H.real, H.imag])

# PCA projection
pca = PCA(n_components=3)
H_pca = pca.fit_transform(H_real)

# Plot 3D manifold
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(H_pca[:,0], H_pca[:,1], H_pca[:,2])
ax.set_title("CSI Manifold (PCA 3D Projection)")
plt.savefig("results/manifold_3d.png")
plt.close()

# Numerical Jacobian
dx = x_positions[1] - x_positions[0]
J_norm = np.linalg.norm(np.gradient(H_real, dx, axis=0), axis=1)

plt.figure()
plt.plot(x_positions, J_norm)
plt.title("Jacobian Norm vs Position")
plt.xlabel("Position")
plt.ylabel("||J(X)||")
plt.grid()
plt.savefig("results/jacobian_heatmap.png")
plt.close()

print("Manifold and Jacobian figures saved.")
