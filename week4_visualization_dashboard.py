"""Week 4: Matplotlib and Seaborn visualizations for the weather dataset."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "weather_sample.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    # Seaborn is used for styling; Matplotlib creates the charts for broad compatibility.
    sns.set_theme()
    df = pd.read_csv(DATA_PATH, parse_dates=["date"]).drop_duplicates()
    numeric = ["temperature_c", "humidity", "wind_kmh", "rainfall_mm"]
    for col in numeric:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

    plt.figure(figsize=(8, 5))
    plt.hist(df["temperature_c"], bins=8, edgecolor="black")
    plt.title("Distribution of Daily Temperature")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "temperature_histogram.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    for city, group in df.groupby("city"):
        plt.scatter(group["temperature_c"], group["humidity"], label=city, s=65)
    plt.title("Temperature vs Humidity by City")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Humidity (%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "temperature_humidity_scatter.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    cities = list(df["city"].unique())
    plt.boxplot([df.loc[df["city"] == city, "temperature_c"] for city in cities], tick_labels=cities)
    plt.title("Temperature Range by City")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "city_temperature_boxplot.png", dpi=150)
    plt.close()

    correlation = df[numeric].corr().to_numpy()
    plt.figure(figsize=(7, 5))
    plt.imshow(correlation, aspect="auto", vmin=-1, vmax=1)
    plt.colorbar(label="Correlation")
    plt.xticks(range(len(numeric)), numeric, rotation=30, ha="right")
    plt.yticks(range(len(numeric)), numeric)
    for i in range(len(numeric)):
        for j in range(len(numeric)):
            plt.text(j, i, f"{correlation[i, j]:.2f}", ha="center", va="center")
    plt.title("Weather Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "weather_correlation_heatmap.png", dpi=150)
    plt.close()
    print("Dashboard plots saved in:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
