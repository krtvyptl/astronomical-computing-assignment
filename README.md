
# Astronomical Computing Assignment
This repository contains solutions for the ASTR4004/8004 assignment.

## Task 1: Git in Practice
This task demonstrates the use of Git for version control, including creating branches, committing changes, and merging branches.

# Task 2: Querying Gaia DR3 and Crossmatching with 2MASS for Messier 67

## Overview

This task involved querying the **Gaia DR3** catalog to find bright stars (G < 14) around the **Messier 67** cluster and crossmatching them with the **2MASS** catalog. After retrieving the relevant data, we filtered the stars to keep only those with reliable photometric measurements and positive parallaxes. Finally, we generated two plots to visualize the properties of these stars.

## Objectives

1. Query Gaia DR3 for stars around Messier 67 within a 1-degree radius.
2. Crossmatch the Gaia stars with the 2MASS catalog to retrieve J and Ks magnitudes.
3. Filter stars with bad photometry and non-positive parallaxes.
4. Generate a **Color-Magnitude Diagram (CMD)** and a **J-Ks vs. Apparent K Diagram**.

## Approach

### Step 1: Query Gaia DR3 for Stars Around Messier 67

Using **ADQL** (Astronomical Data Query Language), we queried the **Gaia DR3** catalog for stars located within a 1-degree radius of Messier 67's central coordinates (RA = 132.825, Dec = 11.8). To focus on the brightest stars, we filtered by G-band magnitude, keeping only stars with **G < 14**.



### Step 2: Crossmatch with 2MASS

To enrich the dataset, we crossmatched the Gaia stars with the **2MASS** catalog using the **tmass_psc_xsc_best_neighbour** table in Gaia DR3. This allowed us to retrieve the **J-band** and **Ks-band** magnitudes (`j_m`, `ks_m`) as well as the **2MASS photometry quality flag** (`ph_qual`).

### Step 3: Filter the Data

We applied two filters to clean up the dataset:
1. **Photometry Quality**: We only kept stars with the highest quality photometry from 2MASS (`ph_qual == 'AAA'`).
2. **Positive Parallaxes**: We filtered out stars with non-positive parallaxes (`parallax > 0`), as these can often indicate bad data or issues with distance measurement.

The filtered dataset was saved as `m67_filtered_stars.csv`.

### Step 4: Generate Plots

Two key diagrams were generated to visualize the star properties:
1. **Color-Magnitude Diagram (CMD)**: A plot of G magnitude vs. BP - RP color index (both from Gaia), which shows the star population of Messier 67 across different evolutionary stages.
   
2. **J-Ks vs. Apparent K Diagram**: A plot of Ks magnitude (from 2MASS) vs. J - Ks color index (from 2MASS), which provides another view of the cluster's star population based on infrared magnitudes.

Both plots were saved as `cmds_m67.png` and can be used to analyze the cluster's stellar distribution and evolutionary trends.

### Recommendations to Colleague

Based on the results and experience with this task, I would recommend the following if you plan to do a similar project:
1. **Verify Catalog Crossmatches**: When crossmatching different catalogs (e.g., Gaia and 2MASS), make sure to inspect the available columns to ensure the correct ones (e.g., photometric data) are being retrieved. This will help avoid errors during plotting or analysis.
   
2. **Filter Data Carefully**: Applying appropriate filters (e.g., photometric quality and positive parallax) is crucial to ensure that the dataset is reliable. I found that filtering out stars with bad photometry significantly improved the quality of the analysis.

3. **Visualize Data**: Visualizing the data using both CMD and J-Ks diagrams helped to better understand the properties of the star cluster. Be sure to invert the magnitude axes when plotting, as magnitude is lower for brighter objects.

If you need further help, feel free to check the `task2_adql_query.py` script for detailed comments on how the query and plots were generated.

## Files Generated

- **m67_filtered_stars.csv**: Filtered list of stars with good photometry and positive parallax.
- **cmds_m67.png**: A PNG file containing both the CMD and J-Ks vs. Apparent K plots.


## Summary

This task successfully retrieved stars from the Gaia DR3 catalog, crossmatched them with the 2MASS catalog, and generated visualizations for Messier 67. These diagrams provide insight into the stellar population of the cluster, with the CMD displaying the main sequence and the J-Ks diagram offering another perspective on star properties. The results can be used to further analyze the cluster’s characteristics and its star population.

# Task 3: Radial Metallicity Gradient Analysis in Milky Way Analogue

## Objective
Analyze simulated data of the Milky Way analogue to study the radial metallicity gradient. This involves fitting a linear model to the relationship between gas-phase oxygen abundance (A(O)) and galactocentric radius (RGal), generating residuals, and creating 2D histograms of A(O), fitted values, and residuals.

## Approach
1. **Loading Data**: We loaded the provided FITS file containing x, y, z positions and oxygen abundances.
2. **Galactocentric Radius**: We calculated the galactocentric radius (RGal) from the x, y, and z positions.
3. **Linear Fit**: We fitted a linear model to A(O) as a function of RGal. The slope of the fit was -0.03, indicating a negative gradient in metallicity with increasing radius.
4. **Residual Analysis**: We calculated and plotted the residuals to identify any deviations from the linear fit.
5. **2D Histograms**: We generated histograms of the simulated median A(O), the fitted A(O), and the residuals in the x-y plane.

## Choice of 2D Bins
For the 2D histograms, we chose to use **50 bins** along both the x and y axes. This choice strikes a balance between revealing the key structures in the data (such as the spiral arms) while avoiding over- or under-smoothing.

### Fewer Bins:
With fewer bins (e.g., 20 or 30), the data would be overly smoothed, and fine details—such as the spiral structure and regions of higher metallicity—would be missed. The residuals would also appear overly generalized, obscuring any subtle patterns or deviations from the linear model.

### More Bins:
Using more bins (e.g., 100 or more) would result in over-segmentation. This would create noise in the histograms, especially in areas with fewer data points. As a result, the histograms would become harder to interpret, and the residuals might show spurious variations, which would complicate the analysis without adding meaningful insights.

## Residuals Analysis
### Observations:
The residuals plot reveals a **spiral pattern**, which suggests that the linear model does not fully capture the complexity of the oxygen abundance distribution. Specifically:
- There are regions in the galaxy where the residuals are consistently positive or negative, indicating that the linear model either over- or underestimates the metallicity in certain parts of the galaxy.
- These patterns suggest that the metallicity gradient is not purely linear, and other factors—such as radial migration, star formation, or gas inflow—might be affecting the metallicity distribution.

### Proposed Explanation:
The spiral pattern observed in the residuals is likely due to **radial metallicity gradients** in the spiral arms, where star formation and gas mixing processes affect the local oxygen abundance. In particular:
- **Star Formation**: Spiral arms are regions of active star formation, which can lead to localized increases in metallicity. The linear model, which assumes a smooth gradient, cannot capture these localized variations.
- **Radial Migration**: Stars and gas might migrate within the galaxy, either inflowing toward the center or outward toward the edges, affecting the distribution of metals and creating non-linear patterns that the linear fit cannot model.
- **Non-Linear Effects**: The radial metallicity gradient in real galaxies is often more complex than a simple linear decrease. A more sophisticated, possibly non-linear model might provide a better fit to the data.

## RMSE of the Fit
The RMSE (Root Mean Square Error) of the linear fit was calculated to be **{RMSE_value}**. This gives a quantitative measure of how well the linear model fits the data.

## Files
- `task3_metallicity_analysis.py`: Python script for performing the analysis.
- `metallicity_vs_radius.png`: Galactocentric radius vs. oxygen abundance plot with linear fit.
- `residuals_metallicity_vs_radius.png`: Residuals of the linear fit.
- `metallicity_residuals_histogram.png`: 2D histograms of A(O), fitted values, and residuals.

## Conclusion
The linear model successfully captures the overall trend of decreasing metallicity with increasing galactocentric radius. However, the residuals reveal non-linear patterns, particularly along the spiral arms, which suggest that a more complex model is required to fully explain the metallicity distribution in this galaxy. The chosen bin size (50 bins) provided
