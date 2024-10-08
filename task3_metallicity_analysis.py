from astropy.io import fits
import numpy as np




# Load the FITS file
file_path = "data/nihao_uhd_simulation_g8.26e11_xyz_positions_and_oxygen_ao.fits"
hdul = fits.open(file_path)
data = hdul[1].data

# Extract relevant columns
x = data['x']
y = data['y']
z = data['z']
A_O = data['A_O']  # Oxygen abundance (metallicity)

RGal = np.sqrt(x**2 + y**2 + z**2)


import matplotlib.pyplot as plt
from scipy.stats import linregress
from matplotlib.colors import LogNorm

# Logarithmic density plot
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist2d(RGal, A_O, bins=50, cmap='plasma', norm=LogNorm())
plt.colorbar(label='Density')
plt.xlabel('Galactocentric Radius (RGal) [kpc]')
plt.ylabel('Gas-phase Oxygen Abundance (A(O))')

# Linear fit
slope, intercept, r_value, p_value, std_err = linregress(RGal, A_O)
plt.plot(RGal, intercept + slope * RGal, 'r', label=f'Fit: y={intercept:.2f}+{slope:.2f}x')
plt.legend()

# Save figure
plt.savefig('figures/metallicity_vs_radius.png', dpi=200)
plt.show()

print(f"Slope: {slope}, Intercept: {intercept}")

residuals = A_O - (intercept + slope * RGal)

plt.subplot(1, 2, 2)
plt.scatter(RGal, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Galactocentric Radius (RGal) [kpc]')
plt.ylabel('Residuals ∆A(O)')
plt.title('Residuals of the Linear Fit')
plt.tight_layout()
plt.show()


# Save the plot to file
plt.savefig('figures/metallicity_residuals_fit.png', dpi=200)

from sklearn.metrics import mean_squared_error

# Calculate RMSE for the linear fit
rmse = np.sqrt(mean_squared_error(A_O, intercept + slope * RGal))
print(f"RMSE of the linear fit: {rmse}")


# Create a 3-panel figure
plt.figure(figsize=(18, 6))

# Panel (a): 2D histogram of median A(O)
plt.subplot(1, 3, 1)
plt.hist2d(x, y, bins=50, weights=A_O, cmap='plasma')
plt.colorbar(label='Median A(O)')
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.title('Median Simulated A(O)')

# Panel (b): 2D histogram of fitted A(O)
fitted_A_O = intercept + slope * RGal
plt.subplot(1, 3, 2)
plt.hist2d(x, y, bins=50, weights=fitted_A_O, cmap='plasma')
plt.colorbar(label='Median Fitted A(O)')
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.title('Median Fitted A(O)')

# Panel (c): 2D histogram of residuals
plt.subplot(1, 3, 3)
plt.hist2d(x, y, bins=50, weights=residuals, cmap='plasma')
plt.colorbar(label='Residuals ∆A(O)')
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.title('Residuals ∆A(O)')

plt.tight_layout()
plt.savefig('figures/metallicity_residuals_histogram.png', dpi=200)
plt.show()
