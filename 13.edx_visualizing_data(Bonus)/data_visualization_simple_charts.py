# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:52:06 2019

@author: suleyman.kaya
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

Tum_Data = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

Tum_Data.drop(columns=['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
Tum_Data.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)

Hepsi_String = all(isinstance(column, str) for column in Tum_Data.columns)
Tum_Data.columns = list(map(str, Tum_Data.columns))
Hepsi_String2 = all(isinstance(column, str) for column in Tum_Data.columns)

Tum_Data.set_index('Country', inplace=True)
Tum_Data['Total'] = Tum_Data.sum(axis=1)
Yıl = list(map(str, range(1980, 2014)))
mpl.style.use('ggplot')

#Area Plots
Tum_Data.sort_values(['Total'], ascending=False, axis=0, inplace=True)
Tum_Data2 = Tum_Data.head()
Tum_Data2 = Tum_Data2[Yıl].transpose()

Tum_Data2.index = Tum_Data2.index.map(int)
Tum_Data2.plot(kind="area", stacked=False, figsize=(15, 8), alpha=0.5)
plt.title("En Fazla Göçmen Yollayan Ülkeler")
plt.ylabel("Göçmen Sayısı")
plt.xlabel("Yıl")
plt.show()

"""
area_p = Tum_Data2.plot(kind='area', alpha=0.35, figsize=(20, 10))
area_p.set_title('Immigration Trend of Top 5 Countries')
area_p.set_ylabel('Number of Immigrants')
area_p.set_xlabel('Years')
"""

#Histogram Plots
Tum_Data3 = Tum_Data["2013"]
count, bin_edges = np.histogram(Tum_Data3, bins= 12)

Tum_Data3.plot(kind='hist', figsize=(8, 5), xticks=bin_edges)
plt.title("2013te En Fazla Göçmen Yollayan Ülkeler Histogramı") 
plt.ylabel('Ülkelerin Sayısı') 
plt.xlabel('Göçmenlerin Sayısı') 
plt.show()

#Histogram 2
Tum_Data3.plot.hist()
plt.show()

#Bar Charts
Izlanda = Tum_Data.loc['Iceland', Yıl]

Izlanda.plot(kind='bar', figsize=(15, 9), rot=90)
plt.xlabel('Yıl')
plt.ylabel('Göçmen Sayısı') 
plt.title('İzlanda Göçmen Sayısı')
 
plt.show()

#Bar Yatay
Tum_Data4 =Tum_Data['Total'].tail()
Tum_Data4.plot(kind='barh', figsize=(10, 6))
plt.xlabel('Göçmen Sayısı')
plt.ylabel("Ülkeler") 
plt.title('En Az Göçmen Gönderen Ülkeler')
plt.show()
