# Week 4 — Data Visualization with Matplotlib and Seaborn

## Concepts covered
- **Matplotlib:** Python plotting library used to create and customize charts.
- **Seaborn:** statistical visualization library built on Matplotlib.
- **Histogram:** displays the distribution of a numerical variable.
- **Scatter plot:** helps inspect the relationship between two numerical variables; hue can distinguish categories.
- **Box plot:** summarizes a distribution using quartiles and potential outliers.
- **Heatmap:** uses colour intensity to show values in a matrix, such as a correlation matrix.

## Client-style dashboard
The dashboard script cleans the demonstration weather data and generates four complementary plots:
1. Temperature histogram.
2. Temperature-versus-humidity scatter plot, separated by city.
3. City-wise temperature box plot.
4. Correlation heatmap for numeric weather features.

## How to run
`python Week4_Visualization/week4_visualization_dashboard.py`

The script saves PNG charts in the `outputs/` folder. These charts are a compact static dashboard deliverable; they are not an interactive web dashboard.
