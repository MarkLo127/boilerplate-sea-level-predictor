import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10)

    # Create first line of best fit (for all data) and extend to 2050
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_all = res_all.slope
    intercept_all = res_all.intercept
    years_extended = np.arange(df['Year'].min(), 2051)  # up to and including 2050
    predicted_all = intercept_all + slope_all * years_extended
    plt.plot(years_extended, predicted_all, 'r', label='Fit (all data)')

    # Create second line of best fit (for data from year 2000 onwards) and extend to 2050
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    slope_2000 = res_2000.slope
    intercept_2000 = res_2000.intercept
    years_recent = np.arange(2000, 2051)
    predicted_recent = intercept_2000 + slope_2000 * years_recent
    plt.plot(years_recent, predicted_recent, 'g', label='Fit (2000 onward)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
