
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

