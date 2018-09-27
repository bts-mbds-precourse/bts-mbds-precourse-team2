import csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv('/Users/allison/Desktop/BTS-MBDS/Pre-Course/Project/DataSet/GlobalLandTemperaturesByCity.csv')
# print(data)

df = pd.DataFrame(data, columns=['dt', 'AverageTemperature', "City", "Country"])
rd = df.rename(columns={'dt': "Date", 'AverageTemperature': "AvgTemp", "City": 'City', "Country": 'Country'})
# print(df)

rd["Date"] = pd.to_datetime(rd["Date"])

rd["day"] = rd['Date'].map(lambda x: x.day)
rd["month"] = rd['Date'].map(lambda x: x.month)
rd["year"] = rd['Date'].map(lambda x: x.year)
rd = rd.loc[rd['year'] > 1850]



#temperature data grouped by country and averaged to a yearly mean
temp_stats = rd.groupby(['Country', 'year'])['AvgTemp'].describe()
temp_stats.reset_index(inplace=True)
temp_stats = pd.DataFrame(temp_stats, columns=['Country', 'year', 'mean', 'max'])
print(temp_stats)


USA = temp_stats.loc[temp_stats['Country'] == 'United States']
India = temp_stats.loc[temp_stats['Country'] == 'India']
Nigeria = temp_stats.loc[temp_stats['Country'] == 'Nigeria']
China = temp_stats.loc[temp_stats['Country'] == 'China']
Spain = temp_stats.loc[temp_stats['Country'] == 'Spain']
Venezuela = temp_stats.loc[temp_stats['Country'] == 'Venezuela']

import seaborn as sns


#lineplots means
sns.lineplot(x = 'year', y = 'mean', data = USA, color = 'Blue', label = 'USA')
sns.lineplot(x = 'year', y = 'mean', data = India, color = 'Orange', label = 'India')
sns.lineplot(x = 'year', y = 'mean', data = Nigeria, color = 'Green', label = 'Nigeria')
sns.lineplot(x = 'year', y = 'mean', data = China, color = 'Red', label = 'China')
sns.lineplot(x = 'year', y = 'mean', data = Spain, color = 'Yellow', label = 'Spain')
sns.lineplot(x = 'year', y = 'mean', data = Venezuela, color = 'Purple', label = 'Venezuela')
sns.despine()
plt.title('Average Temperatures 1850 to 2013')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fontsize = 7)
plt.show()

"""
#lineplots max
sns.lineplot(x = 'year', y = 'max', data = Denmark)
sns.lineplot(x = 'year', y = 'max', data = Turkey)
sns.lineplot(x = 'year', y = 'max', data = Kazakhstan)
sns.lineplot(x = 'year', y = 'max', data = China)
sns.lineplot(x = 'year', y = 'max', data = Spain)
sns.lineplot(x = 'year', y = 'max', data = Germany)
plt.title('Maximum Temperatures 1850 to 2013')
plt.ylim(0, 30)
plt.show()


#trendline
sns.regplot(x = 'year', y = 'mean', data = USA, marker=".", x_estimator=np.mean, logx=True, truncate=True, color = 'blue', label = 'USA', scatter_kws={"s": 4})
sns.regplot(x = 'year', y = 'mean', data = India, marker=".", x_estimator=np.mean, logx=True, truncate=True, color = 'orange', label = 'India', scatter_kws={"s": 4})
sns.regplot(x = 'year', y = 'mean', data = Nigeria, marker=".", x_estimator=np.mean, logx=True, truncate=True, color = 'green', label = 'Nigeria', scatter_kws={"s": 4})
sns.regplot(x = 'year', y = 'mean', data = China, marker=".", x_estimator=np.mean, logx=True, truncate=True, color = 'red', label = 'China', scatter_kws={"s": 4})
sns.regplot(x = 'year', y = 'mean', data = Spain, marker=".", x_estimator=np.mean, logx=True, truncate=True, color = 'yellow', label = 'Spain', scatter_kws={"s": 4})
sns.regplot(x = 'year', y = 'mean', data = Venezuela,marker=".", x_estimator=np.mean, logx=True, truncate=True, color = 'purple', label = 'Venezuela', scatter_kws={"s": 4})
sns.despine()
plt.title('Average Temperatures 1850 to 2013')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fontsize = 7)
plt.show()


sns.lmplot(x='year', y="mean", data= USA, order=3, palette = "#4daf4a")
plt.title('USA Average Temperatures 1850 to 2013')
plt.ylim(12, 17)
plt.show()

sns.lmplot(x='year', y="mean", data= India, order=3, palette  = "#1f78b4")
plt.title('India Average Temperatures 1850 to 2013')
plt.ylim(22, 27)
plt.show()

sns.lmplot(x='year', y="mean", data= Nigeria, order=3, palette = "#e41a1c")
plt.title('Nigeria Average Temperatures 1850 to 2013')
plt.ylim(24, 29)
plt.show()

sns.lmplot(x='year', y="mean", data= China, order=3, palette = "#7570b3")
plt.title('China Average Temperatures 1850 to 2013')
plt.ylim(11, 16)
plt.show()

sns.lmplot(x='year', y="mean", data= Spain, order=3, palette = "#YlOrBr")
plt.title('Spain Average Temperatures 1850 to 2013')
plt.ylim(13, 18)
plt.show()

sns.lmplot(x='year', y="mean", data= Venezuela, order=3, palette = "Purples")
plt.title('Venezuela Average Temperatures 1850 to 2013')
plt.ylim(24, 29)
plt.show()

"""


#grouping by ten year intervals
rd = rd.groupby(['Country', pd.cut(rd['year'], np.arange(1850, 2010, 10))])['AvgTemp']
print(list(rd))
rd = rd.apply(pd.DataFrame)
#rd = rd.to_frame()
#rd.reset_index(inplace=True)
#rd = rd.get_group("Denmark")

print(rd.head())

#rd.boxplot()
#plt.show()
USA2 = rd['USA']
India2 = rd['India']
Nigeria2 = rd['Nigeria']
China2 = rd['China']
Venezuela2 = rd['Venezuela']
Spain2 = rd['Spain']



#Boxplots of ten year ranges. One graph per country. 
sns.boxplot(data = USA2, palette='Blues')
sns.despine()
plt.title('United States of America - temperature insight by decade 1850 to 2013')
plt.tick_params(labelsize=7)
plt.xticks(rotation=45)
plt.ylim(-30,30)
plt.show()

sns.boxplot(data = India2, palette='Oranges')
sns.despine()
plt.title('India - temperature insight by decade 1850 to 2013')
plt.tick_params(labelsize=7)
plt.xticks(rotation=45)
plt.ylim(-30,30)
plt.show()

sns.boxplot(data = Nigeria2, palette='Greens')
sns.despine()
plt.title('Nigeria - temperature insight by decade 1850 to 2013')
plt.tick_params(labelsize=7)
plt.xticks(rotation=45)
plt.ylim(-30,30)
plt.show()

sns.boxplot(data = China2, palette='Reds')
sns.despine()
plt.title('China - temperature insight by decade 1850 to 2013')
plt.tick_params(labelsize=7)
plt.xticks(rotation=45)
plt.ylim(-30,30)
plt.show()

sns.boxplot(data = Spain2, palette='YlOrBr')
sns.despine()
plt.title('Spain - temperature insight by decade 1850 to 2013')
plt.tick_params(labelsize=7)
plt.xticks(rotation=45)
plt.ylim(-30,30)
plt.show()

sns.boxplot(data = Venezuela2, palette = 'Purples')
sns.despine()
plt.title('Venezuela - temperature insight by decade 1850 to 2013')
plt.tick_params(labelsize=7)
plt.xticks(rotation=45)
plt.ylim(-30,30)
plt.show()
