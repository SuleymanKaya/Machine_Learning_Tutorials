# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:20:31 2019

@author: suleyman.kaya
"""

import pandas as pd
import folium as fl
from folium import plugins as pg
import json


"""
Tum_Data = fl.Map(location=[56.130, -106.35], zoom_start=4,
                  tiles='Stamen Toner')
Tum_Data.save("Harita.html")

Tum_Data2 = fl.Map(location=[56.130, -106.35], zoom_start=4,
                  tiles='Stamen Terrain')
Tum_Data2.save("Harita2.html")

#İşaretleyici Harita
Emniyet_Olaylar = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')
Emniyet_Olaylar = Emniyet_Olaylar.iloc[0:100,:]

SF1 = fl.Map(location=[37.77, -122.42], zoom_start=12)

for lat1, long1, label1 in zip(Emniyet_Olaylar.Y, Emniyet_Olaylar.X, 
                            Emniyet_Olaylar.Category):
        fl.CircleMarker(
            location= [lat1, long1],
            popup=label1,
            radius=5, 
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        ).add_to(SF1)
    

SF1.save("SF1.html")

#İşaretleyici Harita2
SF2 = fl.Map(location=[37.77, -122.42], zoom_start=12)
Olaylar = pg.MarkerCluster().add_to(SF2)

for lat2, long2, label2, in zip(Emniyet_Olaylar.Y, Emniyet_Olaylar.X, 
                            Emniyet_Olaylar.Category):
    fl.Marker(
        location=[lat2, long2],
        icon=None,
        popup=label2,
    ).add_to(Olaylar)

SF2.save("SF2.html")
"""
#Renk Tonlu Harita
Tum_Data3 = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                     sheet_name='Canada by Citizenship',
                     skiprows=range(20),
                     skipfooter=2)
Tum_Data3.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
Tum_Data3.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)
Tum_Data3.columns = list(map(str, Tum_Data3.columns))
Tum_Data3['Total'] = Tum_Data3.sum(axis=1)
Yıl = list(map(str, range(1980, 2014)))

Tum_Data3.at[143, "Country"] = "Russia"
Tum_Data3.at[183, "Country"] = "United Kingdom"
Tum_Data3.at[81, "Country"] = "Iran"

with open('world_countries.json', "r") as json_file:
    world_geo = json.load(json_file)
    
Data_Json= pd.read_json('world_countries.json')
    
Dunya_Haritası = fl.Map(location=[0, 0], zoom_start=2)
Dunya_Haritası.choropleth(
    geo_data=world_geo,
    data=Tum_Data3,
    columns=['Country', 'Total'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
     nan_fill_color='white',
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Kanadaya Göç',
    reset=True,
     tiles='"http://{s}.tiles.mapbox.com/v4/wtgeographer.2fb7fc73/{z}/{x}/{y}.png?access_token=pk.xxx',
     attr='XXX Mapbox Attribution'
)

Dunya_Haritası.save("Dunya_Haritası.html")

