# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:09:46 2019

@author: suleyman.kaya
"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

Tum_Data = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

Tum_Data.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
Tum_Data.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)
Tum_Data.columns = list(map(str, Tum_Data.columns))
Tum_Data.set_index('Country', inplace=True)
Tum_Data['Total'] = Tum_Data.sum(axis=1)
Yıl = list(map(str, range(1980, 2014)))
mpl.style.use('ggplot')

#1. Pasta Grafik 
Kitalar = Tum_Data.groupby('Continent', axis=0).sum().head()
Kitalar['Total'].plot(kind='pie', figsize=(5, 6), autopct='%1.1f%%', 
                        startangle=90, shadow=True)

plt.title('Kıtalara Göre 1980 - 2013 Arası Kanadaya Göçler')
plt.axis('equal')
plt.show()

#1. Pasta Grafik 2
Renkler = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.3, 0.3, 0, 0, 0.1]

Kitalar['Total'].plot(kind='pie',figsize=(15, 6), autopct='%1.1f%%', 
                            startangle=90,    
                            shadow= True,       
                            labels=None,         
                            pctdistance=1.12,
                            explode=explode_list,
                            colors=Renkler)

plt.title('Kıtalara Göre 1980 - 2013 Arası Kanadaya Göçler', y=1.3) 
plt.axis('equal')
plt.legend(labels=Kitalar.index, loc='upper left') 
plt.show()

#2. Kutu Grafik

Avrupa_Afrika = Kitalar.loc[["Europe", "Africa"], Yıl].transpose()
İstatiskleri= Avrupa_Afrika.describe()
Avrupa_Afrika.plot(kind="box", figsize=(8,6))
plt.title("1980'dan 2013'e Avrupalı Göçmen Sayısı")
plt.ylabel("Göçmen Sayısı")
plt.show()

#2. Kutu Grafik 2

Avrupa_Afrika = Kitalar.loc[["Europe", "Africa"], Yıl].transpose()
Avrupa_Afrika.plot(kind="box", figsize=(8,6), color="blue", vert=False)
plt.title("1980'dan 2013'e Avrupalı Göçmen Sayısı")
plt.xlabel("Göçmen Sayısı")
plt.show()

# Karşılaştırmalı Grafik

Sekil= plt.figure()
ax0 = Sekil.add_subplot(1, 2, 1) 
ax1 = Sekil.add_subplot(122)

Avrupa_Afrika.plot(kind="box", figsize=(20, 6), color="blue", vert=False, ax=ax0)
ax0.set_title("1980'dan 2013'e Avrupalı ve Afrikalı Göçmen Sayısı - Kutu Grafiği")
ax0.set_xlabel("Göçmen Sayısı")
ax0.set_ylabel("Kıtalar")


Avrupa_Afrika.plot(kind="line", figsize=(20, 6), ax=ax1)
ax1.set_title("1980'dan 2013'e Avrupalı ve Afrikalı Göçmen Sayısı - Doğrusal Grafik")
ax1.set_ylabel("Göçmen Sayısı")
ax1.set_xlabel("Yıl")

plt.show()

#3. Serpme Grafik
Toplam_Nufus = pd.DataFrame(Tum_Data[Yıl].sum(axis=0))
Toplam_Nufus.index = map(int, Toplam_Nufus.index)
Toplam_Nufus.reset_index(inplace=True)
Toplam_Nufus.columns = ["Yıl", "Toplam"]

Toplam_Nufus.plot(kind="scatter", x="Yıl", y="Toplam", figsize= (7,4), color="darkblue")
plt.title("1980'dan 2013'e Toplam Göçmen Sayısı")
plt.xlabel("Yıllar")
plt.ylabel("Göçmen Sayısı")


x = Toplam_Nufus['Yıl']      
y = Toplam_Nufus['Toplam']     
fit = np.polyfit(x, y, deg=1)

plt.plot(x, fit[0]*x+fit[1], color="red")
plt.show()

#4. Kabarcık Grafikleri

Tum_Data_Tersi = Tum_Data[Yıl].transpose()
Tum_Data_Tersi.index = map(int, Tum_Data_Tersi.index)
Tum_Data_Tersi.index.name = "Yıl"
Tum_Data_Tersi.reset_index(inplace=True)

Brezilya_norm = (Tum_Data_Tersi["Brazil"]-Tum_Data_Tersi["Brazil"].min())/(Tum_Data_Tersi["Brazil"].max()-Tum_Data_Tersi["Brazil"].min()) 

Arjantin_norm = (Tum_Data_Tersi["Argentina"]-Tum_Data_Tersi["Argentina"].min())/(Tum_Data_Tersi["Argentina"].max()-Tum_Data_Tersi["Argentina"].min())

# Brezilya
Brezilya = Tum_Data_Tersi.plot(kind='scatter',
                                x='Yıl',
                                y='Brazil',
                                figsize=(14, 8),
                                alpha=0.5,                  
                                color='green',
                                s=Brezilya_norm * 2000 + 10,   
                                xlim=(1975, 2015)
                                    )

# Arjantin
Arjantin = Tum_Data_Tersi.plot(kind='scatter',
                                x='Yıl',
                                y='Argentina',
                                alpha=0.5,
                                color="blue",
                                s=Arjantin_norm * 2000 + 10,
                                ax = Brezilya
                               )
Arjantin.set_ylabel('Göçmen Sayısı')
Brezilya.set_title("1980'dan 2013'e Brezilyalı ve Arjantinli Göçmen Sayısı - Kabarcık Grafiği")
Brezilya.legend(['Brezilya', 'Arjantin'], loc='upper left', fontsize='x-large')


