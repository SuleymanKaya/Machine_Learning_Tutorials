# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:57:43 2019

@author: suleyman.kaya
"""
import pandas as pd
import numpy as np
import matplotlib.pylab as plt


url= "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
Tum_Data= pd.read_csv(url)
ilk5= Tum_Data.head(5)
son10= Tum_Data.tail(10)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

Tum_Data.columns= headers
Tum_Data.dropna(subset=["price"], axis=0, inplace= True)
Tum_Data.reset_index(drop=True, inplace=True)
print(Tum_Data.shape)
#Tum_Data.to_csv("automobile.csv", index=False)
Veri_Tipleri= Tum_Data.dtypes
Veri_Detayları= Tum_Data.describe()
Veri_Detayları_Hepsi= Tum_Data.describe(include="all")
Veri_Detayları2= Tum_Data[['length', 'compression-ratio']].describe()
#print(Tum_Data.info)

Veri_Hazirlama= Tum_Data.replace("?", np.nan, inplace= True)
missing_data= Tum_Data.isnull()

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

avg_norm_loss= Tum_Data["normalized-losses"].astype("float").mean(axis=0)
Tum_Data["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)
avg_bore=Tum_Data['bore'].astype('float').mean(axis=0)
Tum_Data["bore"].replace(np.nan, avg_bore, inplace=True)

Tum_Data[["bore", "stroke"]] = Tum_Data[["bore", "stroke"]].astype("float")
Tum_Data[["normalized-losses"]] = Tum_Data[["normalized-losses"]].astype("int")
Tum_Data[["price"]] = Tum_Data[["price"]].astype("float")
Tum_Data[["peak-rpm"]] = Tum_Data[["peak-rpm"]].astype("float")

Tum_Data["highway-mpg"] = 235/Tum_Data["highway-mpg"]
Tum_Data.rename(columns={"highway-mpg":"highway-mpg"}, inplace= True)

Tum_Data['length'] = Tum_Data['length']/Tum_Data['length'].max()
Tum_Data['width'] = Tum_Data['width']/Tum_Data['width'].max()

Tum_Data = Tum_Data.dropna(subset=['horsepower'])
Tum_Data["horsepower"]=Tum_Data["horsepower"].astype(int, copy=True)
bins = np.linspace(min(Tum_Data["horsepower"]), max(Tum_Data["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']
Tum_Data['horsepower-binned'] = pd.cut(Tum_Data['horsepower'], bins, labels=group_names, include_lowest=True )
Tum_Data_Bins= Tum_Data[['horsepower','horsepower-binned']]

plt.bar(group_names, Tum_Data["horsepower-binned"].value_counts())
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()

plt.hist(Tum_Data["horsepower"], bins=3)
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()

dummy_variable = pd.get_dummies(Tum_Data["fuel-type"])
dummy_variable.rename(columns={'gas':'gaz', 'diesel':'dizel'}, inplace=True)
Tum_Data = pd.concat([Tum_Data, dummy_variable], axis=1)
#Tum_Data.drop("fuel-type", axis = 1, inplace=True)





