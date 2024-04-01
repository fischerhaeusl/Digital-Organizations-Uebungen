# install scraper

import requests as req
import pandas as pd
from bs4 import BeautifulSoup
import csv

#load website data

url = 'https://api.open-meteo.com/v1/dwd-icon?latitude=47.262691&longitude=11.3947&hourly=temperature_2m,relative_humidity_2m,rain,wind_speed_10m&timezone=Europe%2FBerlin&past_days=7'
response = req.get(url)
data = response.json()

# Daten in CSV speichern

weather_data = response.json()["hourly"] #(siehe Landing Page Wetterseite)
df = pd.DataFrame(weather_data)

# CSV-Datei als Excel speichern
df.to_csv('weather_data.csv', index=False)


print("Die Daten wurden erfolgreich als 'wetterdaten.csv' gespeichert.")

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
   # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
