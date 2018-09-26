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
rd = rd.loc[rd['year'] > 1850]

#to create a list of unique countries in rd
unique_countries = rd.Country.unique()
print(unique_countries)


#temperature data grouped by country and averaged to a yearly mean
temp_stats = rd.groupby(['Country', 'year'])['AvgTemp'].describe()
temp_stats.reset_index(inplace=True)
temp_stats = pd.DataFrame(temp_stats, columns=['Country', 'year', "mean"])
print(temp_stats)



#attempt to plot each country in a different quadrant
#fig, axes = plt.subplots(nrows=1, ncols=1)


Denmark = temp_stats.loc[temp_stats['Country'] == 'Denmark']
Turkey = temp_stats.loc[temp_stats['Country'] == 'Turkey']
Kazakhstan = temp_stats.loc[temp_stats['Country'] == 'Kazakhstan']
China = temp_stats.loc[temp_stats['Country'] == 'China']
Spain = temp_stats.loc[temp_stats['Country'] == 'Spain']
Germany = temp_stats.loc[temp_stats['Country'] == 'Germany']

"""
plt.plot('year', 'mean', data = Denmark, linewidth=0.7)
plt.plot('year', 'mean', data = Turkey, linewidth=0.7)
plt.plot('year', 'mean', data = Kazakhstan, linewidth=0.7)
plt.plot('year', 'mean', data = China, linewidth=0.7)
plt.plot('year', 'mean', data = Spain, linewidth=0.7)
plt.plot('year', 'mean', data = Germany, linewidth=0.7)
plt.xlabel("Year")
plt.ylabel("Average Temperature")
plt.legend(('Denmark', 'Turkey', 'Kazakhstan', 'China', 'Spain', 'Germany'))
plt.title('Average Country Temperature 1850 - 2013')
plt.show()


sns.barplot(x = 'year', y = 'mean', data = Denmark)
sns.barplot(x = 'year', y = 'mean', data = Turkey)
sns.barplot(x = 'year', y = 'mean', data = Kazakhstan)
sns.barplot(x = 'year', y = 'mean', data = China)
sns.barplot(x = 'year', y = 'mean', data = Spain)
sns.barplot(x = 'year', y = 'mean', data = Germany)
"""
sns.boxplot(x="year", y="mean", data=Denmark)
plt.show()