"""Space Data Analysis project.

This script downloads real public exoplanet data from the NASA Exoplanet Archive,
creates simple summary statistics and saves a few charts.
"""

from pathlib import Path
from urllib.parse import quote

import matplotlib.pyplot as plt
import pandas as pd
import requests


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
DATA_PATH = DATA_DIR / "exoplanets.csv"
SUMMARY_PATH = OUTPUT_DIR / "summary.txt"

QUERY = """
select pl_name, hostname, disc_year, discoverymethod,
       pl_orbper, pl_rade, pl_bmasse, st_teff
from pscomppars
where disc_year is not null
""".strip()

DATA_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=" + quote(QUERY) + "&format=csv"


def download_data() -> pd.DataFrame:
    """Download exoplanet data from the NASA Exoplanet Archive."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    response = requests.get(DATA_URL, timeout=60)
    response.raise_for_status()

    DATA_PATH.write_bytes(response.content)
    return pd.read_csv(DATA_PATH)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean basic columns and remove impossible values."""
    cleaned = df.copy()
    cleaned["disc_year"] = pd.to_numeric(cleaned["disc_year"], errors="coerce")
    cleaned = cleaned.dropna(subset=["disc_year"])
    cleaned["disc_year"] = cleaned["disc_year"].astype(int)

    for column in ["pl_orbper", "pl_rade", "pl_bmasse", "st_teff"]:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    return cleaned


def save_summary(df: pd.DataFrame) -> None:
    """Save a short text summary of the dataset."""
    total_planets = len(df)
    first_year = int(df["disc_year"].min())
    latest_year = int(df["disc_year"].max())
    top_methods = df["discoverymethod"].value_counts().head(5)

    earth_like = df[
        (df["pl_rade"].between(0.8, 1.5))
        & (df["pl_bmasse"].between(0.5, 5.0))
    ]

    lines = [
        "Space Data Analysis Summary",
        "===========================",
        f"Total confirmed planets in dataset: {total_planets}",
        f"Discovery year range: {first_year} to {latest_year}",
        "",
        "Top discovery methods:",
    ]

    for method, count in top_methods.items():
        lines.append(f"- {method}: {count}")

    lines.extend(
        [
            "",
            f"Simple Earth-like candidates by radius and mass filter: {len(earth_like)}",
            "",
            "Note: This is a beginner-friendly filter, not a real habitability model.",
        ]
    )

    SUMMARY_PATH.write_text("\n".join(lines), encoding="utf-8")


def plot_discoveries_by_year(df: pd.DataFrame) -> None:
    counts = df["disc_year"].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    plt.plot(counts.index, counts.values, marker="o")
    plt.title("Exoplanet discoveries by year")
    plt.xlabel("Discovery year")
    plt.ylabel("Number of planets")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "discoveries_by_year.png", dpi=150)
    plt.close()


def plot_discovery_methods(df: pd.DataFrame) -> None:
    counts = df["discoverymethod"].value_counts().head(10).sort_values()
    plt.figure(figsize=(10, 6))
    plt.barh(counts.index, counts.values)
    plt.title("Top exoplanet discovery methods")
    plt.xlabel("Number of planets")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "discovery_methods.png", dpi=150)
    plt.close()


def plot_planet_radius(df: pd.DataFrame) -> None:
    radius = df["pl_rade"].dropna()
    radius = radius[radius < 30]
    plt.figure(figsize=(10, 5))
    plt.hist(radius, bins=40)
    plt.title("Distribution of planet radius")
    plt.xlabel("Planet radius in Earth radii")
    plt.ylabel("Number of planets")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "planet_radius_distribution.png", dpi=150)
    plt.close()


def main() -> None:
    print("Downloading real exoplanet data...")
    raw_df = download_data()
    df = clean_data(raw_df)

    print(f"Rows downloaded: {len(raw_df)}")
    print(f"Rows after cleaning: {len(df)}")

    save_summary(df)
    plot_discoveries_by_year(df)
    plot_discovery_methods(df)
    plot_planet_radius(df)

    print("Done.")
    print(f"CSV saved to: {DATA_PATH}")
    print(f"Summary saved to: {SUMMARY_PATH}")
    print(f"Charts saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
