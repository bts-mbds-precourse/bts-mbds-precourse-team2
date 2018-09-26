import csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set(style="darkgrid")


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
#print(data)

df = pd.DataFrame(data, columns=['dt', 'AverageTemperature', "City", "Country"])
rd = df.rename(columns={'dt': "Date", 'AverageTemperature': "AvgTemp", "City": 'City', "Country": 'Country'})
print(df)

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

def season_plotter(country_string, season_nr_string):

    country_string_df = rd.loc[rd['Country'] == country_string]


    country_string_df["Date"] = pd.to_datetime(country_string_df["Date"])

    country_string_df["day"] = country_string_df['Date'].map(lambda x: x.day)
    country_string_df["month"] = country_string_df['Date'].map(lambda x: x.month)
    country_string_df["year"] = country_string_df['Date'].map(lambda x: x.year)

    country_string_df = country_string_df.loc[country_string_df['year'] > 1850]

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

        country_string_df["season"] = season

    season_finder(country_string_df['month'])


    season_dataframe = country_string_df.loc[country_string_df['season'] == season_nr_string]
    #Aachen_winter.plot(x='Date', y='AvgTemp', style='.')

    season_mean_dataframe = season_dataframe.groupby(["year"]).mean().transform(lambda x: x.fillna(x.interpolate()))

    season_mean_dataframe["year"] = season_mean_dataframe.index
    season_mean_dataframe.index = range(len(season_mean_dataframe))
    season_mean_dataframe = season_mean_dataframe.rolling(10).mean()



    if season_nr_string == "1":
        #season_mean_dataframe.plot(x='year', y='AvgTemp', style='r-.', ax=axes[0, 0], title = "Winter")
        sns.regplot(x='year', y='AvgTemp', data = season_mean_dataframe, ax=axes[0, 0], scatter_kws={"s": 4}).set_title("Winter")
    elif season_nr_string == "2":
        #season_mean_dataframe.plot(x='year', y='AvgTemp', style='b-.', ax=axes[0, 1], title = "Spring")
        sns.regplot(x='year', y='AvgTemp', data=season_mean_dataframe, ax=axes[0, 1], scatter_kws={"s": 4}).set_title("Spring")
    elif season_nr_string == "3":
        #season_mean_dataframe.plot(x='year', y='AvgTemp', style='g-.', ax=axes[1, 0], title = "Summer")
        sns.regplot(x='year', y='AvgTemp', data=season_mean_dataframe, ax=axes[1, 0], scatter_kws={"s": 4}).set_title("Summer")
    elif season_nr_string == "4":
        #season_mean_dataframe.plot(x='year', y='AvgTemp', style='m-.', ax=axes[1, 1], title = "Autumn")
        sns.regplot(x='year', y='AvgTemp', data=season_mean_dataframe, ax=axes[1, 1], scatter_kws={"s": 4}).set_title("Autumn")



"""
    if season_nr_string == "1":
        season_mean_dataframe.plot(x='year', y='AvgTemp', style='r-.', ax=axes[0, 0])
    elif season_nr_string == "2":
        season_mean_dataframe.plot(x='year', y='AvgTemp', style='b-.', ax=axes[0, 0])
    elif season_nr_string == "3":
        season_mean_dataframe.plot(x='year', y='AvgTemp', style='g-.', ax=axes[0, 0])
    elif season_nr_string == "4":
        season_mean_dataframe.plot(x='year', y='AvgTemp', style='m-.', ax=axes[0, 0])

    def make_plot(axs):
        box = dict(facecolor='yellow', pad=5, alpha=0.2)

        if season_nr_string == "1":
            ax1 = axs[0, 0]
            ax1.plot(x='year', y='AvgTemp', style='r-.',)
            ax1.set_title('ylabels not aligned')
            ax1.set_ylabel('misaligned 1', bbox=box)

        elif season_nr_string == "2":
            ax3 = axs[1, 0]
            ax3.set_ylabel('misaligned 2', bbox=box)
            ax3.plot(x='year', y='AvgTemp', style='r-.',)

        elif season_nr_string == "3":
            ax2 = axs[0, 1]
            ax2.set_title('ylabels aligned')
            ax2.plot(x='year', y='AvgTemp', style='r-.',)
            ax2.set_ylabel('aligned 1', bbox=box)

        elif season_nr_string == "4":
            ax4 = axs[1, 1]
            ax4.plot(x='year', y='AvgTemp', style='r-.',)
            ax4.set_ylabel('aligned 2', bbox=box)

    # Plot 1:
    fig, axs = plt.subplots(2, 2)
    fig.subplots_adjust(left=0.2, wspace=0.6)
    make_plot(int(season_nr_string))

    # just align the last column of axes:
    fig.align_ylabels(axs[:, 1])
    plt.show()
"""
#fig, axes = plt.subplots(nrows=2, ncols=2) #put it here to have one Image with different lines fpr each City.


season_string_list = ["1", "2", "3", "4"]
#country_string_list = ["United States", "India", "China", "Spain", "Nigeria", "Venezuela"]
country_string_list = ["Spain", "Germany", "Turkey", "Kazakhstan", "China"]

for country_name in country_string_list:
    fig, axes = plt.subplots(nrows=2, ncols=2) #leave it here to have a seperate Images for each City
    for season_nr in season_string_list:
        print(country_name)
        season_plotter(country_name, season_nr)
        fig.suptitle(country_name)

plt.show()

