# Space Data Analysis

A beginner-friendly data science project that analyzes real public exoplanet data from the NASA Exoplanet Archive.

## Project goal

This project downloads real exoplanet data and answers questions like:

- How many exoplanets were discovered per year?
- Which discovery methods are most common?
- How are planet radius, mass and orbital period distributed?
- Which planets look most Earth-like based on simple filters?

## Data source

The project uses public data from the NASA Exoplanet Archive, operated by NASA/IPAC/NExScI. The Python script downloads the data from the archive API as CSV.

## Files

- README.md: project explanation
- requirements.txt: Python dependencies
- src/exoplanet_analysis.py: main analysis script
- data/README.md: explains downloaded data
- outputs/README.md: explains generated charts

## How to run

Install dependencies with pip install -r requirements.txt.

Then run python src/exoplanet_analysis.py.

The script downloads real exoplanet data, saves it into the data folder, creates summary statistics and saves charts into the outputs folder.

## Why this is useful

This project shows a real data science workflow: get real public data, clean it, explore it, visualize patterns and write simple conclusions.

It is different from a sales forecast project because it uses astronomy data instead of business data.
