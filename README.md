
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

**ADQL Query**:
```sql
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

