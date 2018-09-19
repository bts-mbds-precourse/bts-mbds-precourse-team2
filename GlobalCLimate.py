import csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
with open('./DataSet/GlobalLandTemperaturesByCity.csv') as csvfile:


file = open('GlobalLandTemperaturesByCity.csv', 'r')
#This is a testing comment...
with open('GlobalLandTemperaturesByCity.csv') as csvfile:

    """sniffer=csv.Sniffer()
    dialect=sniffer.sniff(csvfile.read(2000))"""

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

data = pd.read_csv('./DataSet/GlobalLandTemperaturesByCity.csv')
# print(data)

df = pd.DataFrame(data, columns=['dt', 'AverageTemperature', "City", "Country"])
rd = df.rename(columns={'dt': "Date", 'AverageTemperature': "AvgTemp", "City": 'City', "Country": 'Country'})
# print(df)


# df = pd.read_csv('.\DataSet\GlobalLandTemperaturesByCity.csv', na_values=[' '], names=['dt', 'AverageTemperature', 'City', 'Country'])
Aachen = rd.loc[rd['City'] == 'Aachen']


#rd.plot(x='Date', y='AvgTemp', style='o')
#plt.show()

rd["Date"] = pd.to_datetime(rd["Date"])

rd["day"] = rd['Date'].map(lambda x: x.day)
rd["month"] = rd['Date'].map(lambda x: x.month)
rd["year"] = rd['Date'].map(lambda x: x.year)

print(rd)


#pd.concat([rd.drop('Date', axis = 1),
#(rd.time.str.split("-").str[:3].apply(pd.Series)
#.rename(columns={0:'year', 1:'month', 2:'day'}))], axis = 1)

