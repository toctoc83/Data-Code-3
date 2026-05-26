# Space Data Analysis

A beginner-friendly data science project that analyzes real public exoplanet data from the NASA Exoplanet Archive.

## Project goal

This project downloads real exoplanet data and answers questions like:

- How many exoplanets were discovered per year?
- Which discovery methods are most common?
- How are planet radius, mass and orbital period distributed?
- Which star systems have many known planets?
- Which planets look most Earth-like based on simple filters?

## Data source

The project uses public data from the NASA Exoplanet Archive, operated by NASA/IPAC/NExScI. The Python script downloads the data from the archive API as CSV.

## Files

- README.md: project explanation
- requirements.txt: Python dependencies
- src/exoplanet_analysis.py: main analysis script
- data/README.md: explains downloaded data
- outputs/README.md: explains generated charts and tables

## Current included outputs

The repository already contains a small output snapshot:

- outputs/summary.txt
- outputs/exoplanet_snapshot.csv
- outputs/exoplanet_snapshot_chart.svg

When the Python script is run locally, it can create more detailed generated outputs, including charts and CSV tables.

## How to run

Install dependencies with pip install -r requirements.txt.

Then run python src/exoplanet_analysis.py.

The script downloads real exoplanet data, saves it into the data folder, creates summary statistics and saves charts into the outputs folder.

## Generated outputs from the script

- data/exoplanets.csv
- outputs/summary.txt
- outputs/discoveries_by_year.png
- outputs/discovery_methods.png
- outputs/planet_radius_distribution.png
- outputs/top_star_systems.csv
- outputs/earth_like_candidates.csv

## Why this is useful

This project shows a real data science workflow: get real public data, clean it, explore it, visualize patterns and write simple conclusions.

It is different from a sales forecast project because it uses astronomy data instead of business data.
