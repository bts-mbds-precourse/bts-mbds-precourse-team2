import csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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
temp_stats = rd.groupby(['Country','year'])['AvgTemp'].describe()
temp_stats["year"] = temp_stats.index
temp_stats.index = range(len(temp_stats))

print(temp_stats)

#trying to see what happens when plot all data
temp_stats.plot(x='year', y='AvgTemp', style='-.')
plt.show()

#attempt to plot each country in a different quadrant
fig, axes = plt.subplots(nrows=3, ncols=2)

for c in temp_stats(Country):
    if c == "Denmark":
        temp_stats.plot(x='year', y='AvgTemp', style='r-.', ax=axes[0, 0])
    elif c == "Turkey":
        temp_stats.plot(x='year', y='AvgTemp', style='b-.', ax=axes[0, 1])
    elif c == "Kazakhstan":
        temp_stats.plot(x='year', y='AvgTemp', style='g-.', ax=axes[1, 0])
    elif c == "China":
        temp_stats.plot(x='year', y='AvgTemp', style='m-.', ax=axes[1, 1])
    elif c == "Spain":
        temp_stats.plot(x='year', y='AvgTemp', style='y-.', ax=axes[2, 0])
    elif c == "Germany":
        temp_stats.plot(x='year', y='AvgTemp', style='p-.', ax=axes[2, 1])

plt.show()


