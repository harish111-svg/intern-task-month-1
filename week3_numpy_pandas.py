"""Week 3: NumPy arrays and Pandas data manipulation."""

from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "weather_sample.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    # NumPy arrays, vectorized operations, and broadcasting
    readings = np.array([24.0, 26.0, 28.0, 30.0])
    print("NumPy array:", readings)
    print("Array + 2:", readings + 2)
    print("Array mean:", np.mean(readings))
    print("Broadcasting (array * 1.8 + 32):", readings * 1.8 + 32)

    # Pandas DataFrame and Series
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    print("\nOriginal dataset preview:\n", df.head())
    print("\nTemperature Series:\n", df["temperature_c"])

    # Indexing and inspection
    print("\nSelected columns:\n", df[["city", "temperature_c"]])
    print("\nRows with temperature >= 28:\n", df.loc[df["temperature_c"] >= 28])

    # Data cleaning: remove duplicates, convert numeric fields, fill missing values
    df = df.drop_duplicates().copy()
    numeric_columns = ["temperature_c", "humidity", "wind_kmh", "rainfall_mm"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

    # Aggregation and grouping
    city_summary = (
        df.groupby("city", as_index=False)
          .agg(
              average_temperature_c=("temperature_c", "mean"),
              average_humidity=("humidity", "mean"),
              total_rainfall_mm=("rainfall_mm", "sum"),
              reading_count=("temperature_c", "count"),
          )
    )
    city_summary["average_temperature_c"] = city_summary["average_temperature_c"].round(2)
    city_summary["average_humidity"] = city_summary["average_humidity"].round(2)

    cleaned_path = OUTPUT_DIR / "weather_cleaned.csv"
    summary_path = OUTPUT_DIR / "city_weather_summary.csv"
    df.to_csv(cleaned_path, index=False)
    city_summary.to_csv(summary_path, index=False)

    print("\nCleaned data saved to:", cleaned_path)
    print("\nCity aggregation:\n", city_summary)
    print("Summary saved to:", summary_path)

if __name__ == "__main__":
    main()
