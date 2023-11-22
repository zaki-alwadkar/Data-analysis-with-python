import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create lines of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.arange(df['Year'].min(), 2050, 1)
    y = x * line.slope + line.intercept

    plt.plot(x, y, label='Best Fit Line')

    # Create line of best fit for the years >= 2000
    df_2000 = df[df['Year'] >= 2000]

    line_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2000 = np.arange(2000, 2050, 1)
    y_2000 = x_2000 * line_2000.slope + line_2000.intercept

    plt.plot(x_2000, y_2000, label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Call the function to generate the plot
draw_plot()
plt.show()  # This line is necessary for displaying the plot when running the script outside a Jupyter environment
