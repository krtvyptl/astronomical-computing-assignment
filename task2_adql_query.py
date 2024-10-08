from astroquery.gaia import Gaia

# ADQL query to fetch stars brighter than G = 14 within 1 degree of Messier 67
query = """
SELECT gaia.*, tmass.j_m, tmass.ks_m, tmass.ph_qual
FROM gaiadr3.gaia_source AS gaia
JOIN gaiadr3.tmass_psc_xsc_best_neighbour AS xmatch
ON gaia.source_id = xmatch.source_id
JOIN gaiadr1.tmass_original_valid AS tmass
ON tmass.designation = xmatch.original_ext_source_id
WHERE CONTAINS(
  POINT('ICRS', gaia.ra, gaia.dec),
  CIRCLE('ICRS', 132.825, 11.8, 1)) = 1
AND gaia.phot_g_mean_mag < 14
"""




job = Gaia.launch_job(query)
results = job.get_results()

# Save results to a CSV file
results.write("data/m67_gaia_stars.csv", format="csv", overwrite=True)



import pandas as pd

# Load the CSV data and display the first few rows
data = pd.read_csv("data/m67_gaia_stars.csv")
print(data.head())


# Filter stars with bad 2MASS photometry and non-positive parallaxes
filtered_stars = results[(results['parallax'] > 0) & (results['ph_qual'] == 'AAA')]

# Save filtered data
# Save the filtered data and allow overwriting the file
filtered_stars.write("data/m67_filtered_stars.csv", format="csv", overwrite=True)


import matplotlib.pyplot as plt

# Generate CMD (Gaia BP-RP vs. absolute G magnitude)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(filtered_stars['bp_rp'], filtered_stars['phot_g_mean_mag'])
plt.xlabel('BP - RP')
plt.ylabel('G magnitude')
plt.gca().invert_yaxis()  # Invert y-axis for magnitude
plt.title('CMD')

# Generate J-Ks vs. Apparent K magnitude diagram
plt.subplot(1, 2, 2)
plt.scatter(filtered_stars['j_m'] - filtered_stars['ks_m'], filtered_stars['ks_m'])
plt.xlabel('J - Ks')
plt.ylabel('Ks magnitude')
plt.gca().invert_yaxis()
plt.title('J-Ks vs. Apparent K')
plt.show()


plt.tight_layout()
plt.savefig('figures/cmds_m67.png', dpi=200)
plt.show()

