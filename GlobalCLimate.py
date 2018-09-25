import csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv('.\DataSet\ByCityShort.csv')
# print(data)

df = pd.DataFrame(data, columns=['dt', 'AverageTemperature', "City", "Country"])
rd = df.rename(columns={'dt': "Date", 'AverageTemperature': "AvgTemp", "City": 'City', "Country": 'Country'})
# print(df) 

rd["Date"] = pd.to_datetime(rd["Date"])

rd["day"] = rd['Date'].map(lambda x: x.day)
rd["month"] = rd['Date'].map(lambda x: x.month)
rd["year"] = rd['Date'].map(lambda x: x.year)


#to create a list of unique countries in rd
unique_countries = rd.Country.unique()
print(unique_countries)

#temperature data grouped by country and averaged to a yearly mean
temp_stats = rd.groupby(['Country', 'year'])['AvgTemp'].describe()
temp_stats.reset_index(inplace=True)
temp_stats = pd.DataFrame(temp_stats, columns=['Country', 'year', "mean"])
print(temp_stats)

#attempt to plot each country in a different quadrant
fig, axes = plt.subplots(nrows=1, ncols=1)


Denmark = temp_stats.loc[temp_stats['Country'] == 'Denmark']
Turkey = temp_stats.loc[temp_stats['Country'] == 'Turkey']
Kazakhstan = temp_stats.loc[temp_stats['Country'] == 'Kazakhstan']
China = temp_stats.loc[temp_stats['Country'] == 'China']
Spain = temp_stats.loc[temp_stats['Country'] == 'Spain']
Germany = temp_stats.loc[temp_stats['Country'] == 'Germany']

"""
plt.plot('year', 'mean', data = Denmark)
plt.plot('year', 'mean', data = Turkey)
plt.plot('year', 'mean', data = Kazakhstan)
plt.plot('year', 'mean', data = China)
plt.plot('year', 'mean', data = Spain)
plt.plot('year', 'mean', data = Germany)
plt.show()
"""

sns.lineplot(x = 'year', y = 'mean', data = Denmark)
sns.lineplot('year', 'mean', data = Turkey)
sns.lineplot('year', 'mean', data = Kazakhstan)
sns.lineplot('year', 'mean', data = China)
sns.lineplot('year', 'mean', data = Spain)
sns.lineplot('year', 'mean', data = Germany)
