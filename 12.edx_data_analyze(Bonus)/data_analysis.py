# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:57:23 2019

@author: suleyman.kaya
"""

import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from scipy import stats

url='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
Tum_Data= pd.read_csv(url)
Veri_Turleri= Tum_Data.dtypes

Korelasyon= Tum_Data.corr()
Korelasyon1= Tum_Data[['bore','stroke' ,'compression-ratio','horsepower']].corr()

Korelasyon2= Tum_Data[["engine-size", "price"]].corr()
sns.regplot(x="engine-size", y="price", data= Tum_Data)
#plt.ylim(0,)
plt.show()

Korelasyon3= Tum_Data[["highway-mpg", "price"]].corr()
sns.regplot(x="highway-mpg", y="price", data=Tum_Data)
plt.show()

Korelasyon4= Tum_Data[["peak-rpm", "price"]].corr()
sns.regplot(x="peak-rpm", y="price", data=Tum_Data)
plt.show()

Korelasyon5= Tum_Data[["stroke","price"]].corr()
sns.regplot(x="stroke", y="price", data=Tum_Data )
plt.show()

#Kategorik Verilerin Görselleştirilmesi
sns.boxplot(x="body-style", y="price", data= Tum_Data)
plt.show()

Verinin_Betimlenmesi= Tum_Data.describe(include="all")
Verinin_Betimlenmesi1= Tum_Data.describe()
Verinin_Betimlenmesi2= Tum_Data.describe(include=["object"])

Veri_Sayisi1= Tum_Data['drive-wheels'].value_counts().to_frame()
Veri_Sayisi1.rename(columns={"drive-wheels":"value_counts"}, inplace=True)
Veri_Sayisi1.index.name = 'drive-wheels'


print(Tum_Data['drive-wheels'].unique())
Gurup1= Tum_Data[['drive-wheels','body-style','price']].groupby(['drive-wheels','body-style'], as_index=False).mean()
Gurup2= Tum_Data[['drive-wheels','body-style','price']].groupby(['drive-wheels'], as_index=False).mean()
Pivot1= Tum_Data[['drive-wheels','body-style','price']].pivot_table(index='drive-wheels', columns='body-style').fillna(0)

plt.pcolor(Pivot1, cmap="RdBu")
plt.colorbar()
plt.show()

pearson_coef1, p_value1 = stats.pearsonr(Tum_Data['wheel-base'], Tum_Data['price'])
p_value11= p_value1 < 0.001

pearson_coef2, p_value2 = stats.pearsonr(Tum_Data['horsepower'], Tum_Data['price'])
p_value21= p_value2 < 0.001

#ANOVA
Gurup3= Tum_Data[['drive-wheels','price']].groupby(['drive-wheels'])

Gurup31= Gurup3.get_group('4wd')['price']
Gurup32= Gurup3.get_group('rwd')['price']
Gurup33= Gurup3.get_group('fwd')['price']

F_test_score, P_value = stats.f_oneway(Gurup31,Gurup32, Gurup33)
print("\nANOVA results: F=", F_test_score, ", P =", P_value, P_value<0.001)   
