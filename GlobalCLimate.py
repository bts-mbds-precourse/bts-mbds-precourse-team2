import csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
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


"""

data = pd.read_csv('./DataSet/ByCityShort.csv')
# print(data)

df = pd.DataFrame(data, columns=['dt', 'AverageTemperature', "City", "Country"])
rd = df.rename(columns={'dt': "Date", 'AverageTemperature': "AvgTemp", "City": 'City', "Country": 'Country'})
# print(df)

# df = pd.read_csv('.\DataSet\GlobalLandTemperaturesByCity.csv', na_values=[' '], names=['dt', 'AverageTemperature', 'City', 'Country'])
Aachen = rd.loc[rd['City'] == 'Aachen']


#rd.plot(x='Date', y='AvgTemp', style='o')
#plt.show()

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

Aachen_winter = Aachen.loc[Aachen['season'] == '1']
#Aachen_winter.plot(x='Date', y='AvgTemp', style='.')

Aachen_winter_mean = Aachen_winter.groupby(["year"]).mean()
print(Aachen_winter_mean)


#Aachen_winter_1950 = Aachen_winter.loc[Aachen_winter['year'] == range(1950,2000)]
#Aachen_winter_1950.plot(x='Date', y='AvgTemp', style='o')

plt.show()


#print(rd)

