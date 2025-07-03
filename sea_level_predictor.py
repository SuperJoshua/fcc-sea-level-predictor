import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

pd.options.mode.copy_on_write = True

def draw_plot():
   # Read data from file
   df = pd.read_csv('epa-sea-level.csv')

   # Create scatter plot
   fig, ax = plt.subplots()
   plt.scatter('Year', 'CSIRO Adjusted Sea Level', data = df)

   # Create first line of best fit
   result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
   run = list(range(df['Year'].min(), 2051))
   rise = [result.slope * a + result.intercept for a in run]
   plt.plot(run, rise)

   # Create second line of best fit
   x = df.loc[df['Year'] >= 2000, 'Year']
   y = df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level']
   result = linregress(x, y)
   run = list(range(2000, 2051))
   rise = [result.slope * a + result.intercept for a in run]
   plt.plot(run, rise)

   # Add labels and title
   ax.set_title('Rise in Sea Level')
   ax.set_xlabel('Year')
   ax.set_ylabel('Sea Level (inches)')
   
   # Save plot and return data for testing (DO NOT MODIFY)
   plt.savefig('sea_level_plot.png')
   return plt.gca()
   