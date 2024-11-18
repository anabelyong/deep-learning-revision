import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

# Parameters
radius = 1  # Set radius of sphere/hypercube to 1 for simplicity
dimensions = np.arange(1, 50, 1)  # Dimensionality from 1 to 50

# Volume of hypercube
volumes_hypercube = (2 * radius) ** dimensions

# Volume of hypersphere
volumes_hypersphere = (2 * radius ** dimensions * np.pi ** (dimensions / 2)) / (dimensions * gamma(dimensions / 2))

# Plotting the volumes
plt.figure(figsize=(10, 6))
plt.plot(dimensions, volumes_hypercube, label="HyperCube Volume", marker="o")
plt.plot(dimensions, volumes_hypersphere, label="HyperSphere Volume", marker="x")
print("Volume of Hypercube:", volumes_hypercube)
print("Volume of Hypersphere:", volumes_hypersphere)
plt.yscale("log")  # Use logarithmic scale for better visibility
plt.xlabel("Dimensions (d)")
plt.ylabel("Volume (log scale)")
plt.title("Volume of Hypercube vs Hypersphere as Dimensions Increase")
plt.legend()
plt.grid(True)
plt.show()
