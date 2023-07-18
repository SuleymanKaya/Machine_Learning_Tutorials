# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:16:17 2019

@author: suleyman.kaya
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

Tum_Data = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
print(Tum_Data.info())
print("-------------1")
print(Tum_Data.columns.values)
print("-------------2")
print(Tum_Data.index.values)
print("-------------3")
print(type(Tum_Data.index.tolist()))
print("-------------4")
print(Tum_Data.shape)
print("-------------5")

Tum_Data.drop(columns=['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
Tum_Data.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
Tum_Data['Total'] = Tum_Data.sum(axis=1)
Bos_elamanlar = Tum_Data.isnull().sum()
Genel_İstatik = Tum_Data.describe()

Ulke= Tum_Data.Country
Ulke2 = Tum_Data["Country"]
Ulke3 = Tum_Data[["Country"]] 

Tum_Data.set_index('Country', inplace=True)
Japonya = Tum_Data.loc['Japan']
Tum_Data.columns = list(map(str, Tum_Data.columns))
Japonya2 = Tum_Data.loc['Japan', ["1980", "1981", "1982", "1983", "1984", "1984"]]

Kosul = Tum_Data['Continent'] == 'Asia'
Filitre = Tum_Data[(Tum_Data['Continent']=='Asia') & (Tum_Data['Region']=='Southern Asia')]


print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0
print("-------------6")

Haiti1 = Tum_Data.loc[["Haiti", "India" ,"China", "Turkey"]]
Haiti1.drop(columns=["Continent","Region","DevName","Total"], axis=1, inplace=True)
Haiti2 = Haiti1.loc["Haiti"]
Haiti3= Haiti1.transpose()
Haiti3.index = Haiti3.index.map(int)

Haiti3.plot(kind='line')
plt.title("4 Ülkeden Gelen Göçmenler")
plt.ylabel('Göçmen Sayısı')
plt.xlabel('Yıl')
plt.text(2003, 8000, '2010 Haiti Depremi')
