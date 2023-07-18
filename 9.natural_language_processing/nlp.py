# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:55:04 2019

@author: suleyman.kaya
"""

import pandas as pd
import numpy as np
import re


yorumlar= pd.read_csv("Lokanta_Yorumlari.csv", error_bad_lines=False)

import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

Biriktir = []

#Veri Ön İşleme
for i in range(1000):
    yorum = re.sub("[^a-zA-Z]", " ", yorumlar['Review'][i])
    yorum = yorum.lower()
    yorum = yorum.split()
    yorum = [ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words("english"))]
    yorum = " ".join(yorum)
    Biriktir.append(yorum)
    
#Öznitelik Çıkarımı
from sklearn.feature_extraction.text import CountVectorizer
cv= CountVectorizer(max_features = 1500)
x = cv.fit_transform(Biriktir).toarray()
y = yorumlar.iloc[:,1].values

#Makine Öğrenmesi
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, random_state=0)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train, y_train)
y_pred = gnb.predict(x_test)

#Sonuçlar
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

