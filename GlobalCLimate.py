import csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""""
with open('./DataSet/GlobalLandTemperaturesByCity.csv') as csvfile:


file = open('GlobalLandTemperaturesByCity.csv', 'r')
#This is a testing comment...
with open('GlobalLandTemperaturesByCity.csv') as csvfile:
    sniffer=csv.Sniffer()
    dialect=sniffer.sniff(csvfile.read(2000))
    readCSV = csv.reader(csvfile,delimiter=',', quoting=csv.QUOTE_NONE)
    dt = []
    AverageTemperature = []
    AverageTemperatureUncertainty = []
    City = []
    Country = []
    Latitude = []
    Longitude = []
    i=0
    for row in readCSV:
        i+=1
        date = row[0]
        print(date)
        temperaturamedia = row[1]
        temperaturamedianoexacta = row[2]
        ciudad = row[3]
        pais= row[4]
        latitud = row[5]
        longitud = row[6]

        dt.append(date)
        AverageTemperature.append(temperaturamedia)
        AverageTemperatureUncertainty.append(temperaturamedianoexacta)
        City.append(ciudad)
        Country.append(pais)
        Latitude.append(latitud)
        Longitude.append(longitud)

    print(dt)


"""""


data = pd.read_csv('./DataSet/ByCityShort.csv')
#print(data)


df = pd.DataFrame(data, columns=['dt', 'AverageTemperature', "City", "Country"])
rd = df.rename(columns={'dt': "Date", 'AverageTemperature': "AvgTemp", "City": 'City', "Country": 'Country'})
#print(df)

"""

Aachen = rd.loc[rd['City'] == 'Aachen']

Aachen["Date"] = pd.to_datetime(Aachen["Date"])

Aachen["day"] = Aachen['Date'].map(lambda x: x.day)
Aachen["month"] = Aachen['Date'].map(lambda x: x.month)
Aachen["year"] = Aachen['Date'].map(lambda x: x.year)


def season_finder(month):

    season = []
    for x in month:
        if x == 1 or x == 2 or x == 3:
            season.append("1")
        elif x == 4 or x == 5 or x == 6:
            season.append("2")
        elif x == 7 or x == 8 or x == 9:
            season.append("3")
        elif x == 10 or x == 11 or x == 12:
            season.append("4")

    Aachen["season"] = season

season_finder(Aachen['month'])

print(Aachen)

Aachen_winter = Aachen.loc[Aachen['season'] == '4']
#Aachen_winter.plot(x='Date', y='AvgTemp', style='.')

Aachen_winter_mean = Aachen_winter.groupby(["year"]).mean()

Aachen_winter_mean["year"]=Aachen_winter_mean.index
Aachen_winter_mean.index = range(len(Aachen_winter_mean))
Aachen_winter_mean.plot(x='year', y='AvgTemp', style='-.')

#Aachen_winter_1950 = Aachen_winter.loc[Aachen_winter['year'] == range(1950,2000)]
#Aachen_winter_1950.plot(x='Date', y='AvgTemp', style='o')

plt.show()


"""
fig, axes = plt.subplots(nrows=2, ncols=2)

def season_plotter(city_string, season_nr_string):

    city_string = rd.loc[rd['City'] == city_string]

    city_string["Date"] = pd.to_datetime(city_string["Date"])

    city_string["day"] = city_string['Date'].map(lambda x: x.day)
    city_string["month"] = city_string['Date'].map(lambda x: x.month)
    city_string["year"] = city_string['Date'].map(lambda x: x.year)

    def season_finder(month):

        season = []
        for x in month:
            if x == 1 or x == 2 or x == 3:
                season.append("1") #winter
            elif x == 4 or x == 5 or x == 6:
                season.append("2") #spring
            elif x == 7 or x == 8 or x == 9:
                season.append("3") #summer
            elif x == 10 or x == 11 or x == 12:
                season.append("4") #autumn

        city_string["season"] = season

    season_finder(city_string['month'])


    season_dataframe = city_string.loc[city_string['season'] == season_nr_string]
    #Aachen_winter.plot(x='Date', y='AvgTemp', style='.')

    season_mean_dataframe = season_dataframe.groupby(["year"]).mean()

    season_mean_dataframe["year"] = season_mean_dataframe.index
    season_mean_dataframe.index = range(len(season_mean_dataframe))

    if season_nr_string == "1":
        season_mean_dataframe.plot(x='year', y='AvgTemp', style='r-.', ax=axes[0, 0])
    elif season_nr_string == "2":
        season_mean_dataframe.plot(x='year', y='AvgTemp', style='b-.', ax=axes[0, 1])
    elif season_nr_string == "3":
        season_mean_dataframe.plot(x='year', y='AvgTemp', style='g-.', ax=axes[1, 0])
    elif season_nr_string == "4":
        season_mean_dataframe.plot(x='year', y='AvgTemp', style='m-.', ax=axes[1, 1])



season_string_list = ["1", "2", "3", "4"]

for season_nr in season_string_list:
    season_plotter("Aachen", season_nr)

plt.show()

##########
#Countries changed in temperature per year from the beginning of the dates until nowadays

data = pd.read_csv('./DataSet/ByCityShort.csv',parse_dates=['dt'])

data =data.drop(['AverageTemperatureUncertainty','City','Latitude','Longitude'],1)
data= data.dropna()
#print(data)
#print(data.dtypes)
data['year']=data['dt'].map(lambda x:x.year)
data=data.drop('dt',1)
data=data.dropna()

#print(set(data['Country']))

label=['Turkey', 'Germany', 'Kazakhstan', 'Denmark', 'Spain', 'China']

axy=[]

#Turkey
country1 = data.loc[data['Country'] == 'Turkey' ]
turkey_1=country1.groupby(['year','Country'])['AverageTemperature'].mean().head(1)
turkey_2=country1.groupby(['year','Country'])['AverageTemperature'].mean().tail(1)
y=turkey_2[0]-turkey_1[0]
axy.append(y)

#Germany
country2 = data.loc[data['Country'] == 'Germany' ]
germany_1=country2.groupby(['year','Country'])['AverageTemperature'].mean().head(1)
germany_2=country2.groupby(['year','Country'])['AverageTemperature'].mean().tail(1)
g=germany_2[0]-germany_1[0]
axy.append(g)

#Kazakhstan
country3 = data.loc[data['Country'] == 'Kazakhstan' ]
Kazakhstan_1=country3.groupby(['year','Country'])['AverageTemperature'].mean().head(1)
Kazakhstan_2=country3.groupby(['year','Country'])['AverageTemperature'].mean().tail(1)
k=Kazakhstan_2[0]-Kazakhstan_1[0]
axy.append(k)


#Denmark
country4 = data.loc[data['Country'] == 'Denmark' ]
Denmark_1=country4.groupby(['year','Country'])['AverageTemperature'].mean().head(1)
Denmark_2=country4.groupby(['year','Country'])['AverageTemperature'].mean().tail(1)
d=Denmark_2[0]-Denmark_1[0]
axy.append(d)


#Spain
country5 = data.loc[data['Country'] == 'Spain' ]
Spain_1=country5.groupby(['year','Country'])['AverageTemperature'].mean().head(1)
Spain_2=country5.groupby(['year','Country'])['AverageTemperature'].mean().tail(1)
s=Spain_2[0]-Spain_1[0]
axy.append(s)


#China
country = data.loc[data['Country'] == 'China' ]
china_1=country.groupby(['year','Country'])['AverageTemperature'].mean().head(1)
china_2=country.groupby(['year','Country'])['AverageTemperature'].mean().tail(1)
x=china_2[0]-china_1[0]
axy.append(x)

plt.style.use('dark_background')
plt.bar(label,axy, color='cyan')

plt.ylabel("Temperature change ratio")
plt.xlabel('')
plt.title('Countries with the highest rate of change in temperature')
plt.show()

