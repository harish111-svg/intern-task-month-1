# Week 3 — NumPy and Pandas for Data Manipulation

## Concepts covered
- **NumPy arrays:** efficient numerical collections that support vectorized calculations.
- **Array operations:** calculations can be applied to an entire array without writing an explicit loop.
- **Broadcasting:** NumPy applies compatible scalar or array operations across array elements.
- **Pandas Series:** one-dimensional labelled data.
- **Pandas DataFrame:** two-dimensional tabular data with labelled rows and columns.
- **Indexing:** select columns and filter rows using bracket notation and `.loc`.
- **Grouping:** `groupby()` splits data into groups so aggregate calculations can be performed.

## Hands-on and client-style project
The script reads the supplied weather CSV, demonstrates NumPy operations, removes duplicate rows, converts invalid numeric values to missing values, fills missing numeric entries with column medians, and calculates city-level averages and total rainfall.

## Outputs
- `outputs/weather_cleaned.csv`
- `outputs/city_weather_summary.csv`

The dataset is synthetic demonstration data, not client-provided data.

## How to run
`python Week3_NumPy_Pandas/week3_numpy_pandas.py`
