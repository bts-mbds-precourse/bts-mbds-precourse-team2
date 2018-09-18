import csv
import pandas as pd

"""
with open('./DataSet/GlobalLandTemperaturesByCity.csv') as csvfile:
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
#print(data)

df = pd.DataFrame(data, columns = ['Date', 'MeanTemp', 'City', 'Country',])
#print(df)

#df = pd.read_csv('./DataSet/GlobalLandTemperaturesByCity.csv', na_values=[' '], names=['dt', 'AverageTemperature', 'City', 'Country'])
Aachen = df.loc[df['City'] == 'Aachen']