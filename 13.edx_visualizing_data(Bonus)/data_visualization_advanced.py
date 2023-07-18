# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:28:09 2019

@author: suleyman.kaya
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
from pywaffle import Waffle
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import seaborn as sns


Tum_Data = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)


Tum_Data.drop(['AREA','REG','DEV','Type','Coverage'], axis = 1, inplace = True)
Tum_Data.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace = True)
Tum_Data.columns = list(map(str, Tum_Data.columns))
Tum_Data.set_index('Country', inplace = True)
Tum_Data['Total']= Tum_Data.sum(axis=1)
Yıl = list(map(str, range(1980, 2014)))

mpl.style.use('ggplot')

#Waffle Grafiği
Iskandinavya = Tum_Data.loc[['Denmark', 'Norway', 'Sweden'],:]
Toplam_IskGocu = sum(Iskandinavya['Total'])
Oranlar =pd.DataFrame([(float(value)/Toplam_IskGocu) for value in Iskandinavya['Total']])*100
Oranlar.rename(columns={0:'Ulke_Oranlari'}, inplace = True)
Oranlar.Ulke_Oranlari = Oranlar.Ulke_Oranlari.astype(int)
Oranlar2 = Oranlar["Ulke_Oranlari"].tolist()

data_isk = {'Danimarka': Oranlar2[0], 'Norveç': Oranlar2[1], 'İsveç':Oranlar2[2]}
Waffle_Grafigi = plt.figure(figsize=(12, 8), 
    FigureClass=Waffle, 
    rows=5, 
    values=data_isk, 
    colors=("#983D3D", "#232066", "#DCB732"),
    title={'label': 'İskandinavya Ülkelerinin Kanadaya Toplam Göçmen Sayısı', 'loc': 'left'},
    labels=["{0} ({1}%)".format(k, v) for k, v in data_isk.items()],
    legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data_isk), 'framealpha': 0}
)
Waffle_Grafigi.gca().set_facecolor('#EEEEEE')
Waffle_Grafigi.set_facecolor('#EEEEEE')
plt.show()

#Word Clouds Grafiği
Tum_Data2 = open('alice_novel.txt', 'r').read()
Tum_Data3 = np.array(Image.open('alice_mask.png'))
stopwords = set(STOPWORDS)

alice_wc = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords, mask=Tum_Data3
)

stopwords.add('said')
Kelime_Bulutu = plt.figure()
Kelime_Bulutu.set_figwidth(14)
Kelime_Bulutu.set_figheight(18)

alice_wc.generate(Tum_Data2)

plt.imshow(Tum_Data3, cmap=plt.cm.gray, interpolation='bilinear')
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()

#Regresyon Grafiği
Toplam = pd.DataFrame(Tum_Data[Yıl].sum(axis=0))
Toplam.index = map(float, Toplam.index)
Toplam.reset_index(inplace=True)
Toplam.columns = ['year', 'total']

plt.figure(figsize=(15, 10))
sns.set(font_scale=1.5)
sns.set_style('whitegrid')
Regresyon_Grafigi = sns.regplot(x='year', y='total', data=Toplam, color='green', marker='+', scatter_kws={'s': 200})
Regresyon_Grafigi.set(xlabel='Yıl', ylabel='Toplam Göçmen')
Regresyon_Grafigi.set_title('1980 - 2013 Yılları Arasında Kanadaya Göç Eden Toplam Göçmen Sayısı')





