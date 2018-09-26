import csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv('/Users/allison/Desktop/BTS-MBDS/Pre-Course/Project/DataSet/ByCityShort.csv')
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

"""
#ten year rolling means. apply to the above block of code please
season_mean_dataframe = season_dataframe.groupby(["year"]).mean().transform(lambda x: x.fillna(x.interpolate()))

season_mean_dataframe["year"] = season_mean_dataframe.index
season_mean_dataframe.index = range(len(season_mean_dataframe))
season_mean_dataframe = season_mean_dataframe.rolling(10).mean()
"""

Denmark = temp_stats.loc[temp_stats['Country'] == 'Denmark']
Turkey = temp_stats.loc[temp_stats['Country'] == 'Turkey']
Kazakhstan = temp_stats.loc[temp_stats['Country'] == 'Kazakhstan']
China = temp_stats.loc[temp_stats['Country'] == 'China']
Spain = temp_stats.loc[temp_stats['Country'] == 'Spain']
Germany = temp_stats.loc[temp_stats['Country'] == 'Germany']


import seaborn as sns

#lineplots
sns.lineplot(x = 'year', y = 'mean', data = Denmark)
sns.lineplot(x = 'year', y = 'mean', data = Turkey)
sns.lineplot(x = 'year', y = 'mean', data = Kazakhstan)
sns.lineplot(x = 'year', y = 'mean', data = China)
sns.lineplot(x = 'year', y = 'mean', data = Spain)
sns.lineplot(x = 'year', y = 'mean', data = Germany)
plt.title('Average Temperatures 1850 to 2013')
plt.show()

#trendline
sns.regplot(x = 'year', y = 'mean', data = Denmark, marker=".", x_estimator=np.mean, logx=True, truncate=True)
sns.regplot(x = 'year', y = 'mean', data = Turkey, marker=".", x_estimator=np.mean, logx=True, truncate=True)
sns.regplot(x = 'year', y = 'mean', data = Kazakhstan, marker=".", x_estimator=np.mean, logx=True, truncate=True)
sns.regplot(x = 'year', y = 'mean', data = China, marker=".", x_estimator=np.mean, logx=True, truncate=True)
sns.regplot(x = 'year', y = 'mean', data = Spain, marker=".", x_estimator=np.mean, logx=True, truncate=True)
sns.regplot(x = 'year', y = 'mean', data = Germany,marker=".", x_estimator=np.mean, logx=True, truncate=True)
plt.title('Average Temperatures 1850 to 2013')
plt.show()

"""
#grouping by ten year intervals
tens = rd.groupby([pd.cut(rd['year'], np.arange(1850, 2010, 10), 'Country')])
print(list(tens))
tens = tens.to_frame()
tens.reset_index(inplace=True)
"""

Denmark2 = tens.loc[tens['Country'] == 'Denmark']
Turkey2 = tens.loc[tens['Country'] == 'Turkey']
Kazakhstan2 = tens.loc[tens['Country'] == 'Kazakhstan']
China2 = tens.loc[tens['Country'] == 'China']
Spain2 = tens.loc[tens['Country'] == 'Spain']
Germany2 = tens.loc[tens['Country'] == 'Germany']


"""
#Boxplots of ten year ranges. One graph per country. 
sns.boxplot(x = 'year', y = 'AvgTemp', data = Denmark2)
sns.boxplot(x = 'year', y = 'AvgTemp', data = Turkey2)
sns.boxplot(x = 'year', y = 'AvgTemp', data = Kazakhstan2)
sns.boxplot(x = 'year', y = 'AvgTemp', data = China2)
sns.boxplot(x = 'year', y = 'AvgTemp', data = Spain2)
sns.boxplot(x = 'year', y = 'AvgTemp', data = Germany2)
plt.show()
"""