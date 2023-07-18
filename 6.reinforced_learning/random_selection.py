# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:57:29 2019

@author: suleyman.kaya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler=pd.read_csv('reklamverisi.csv')

import random

N= 10000
d=10
secilenler=[]
toplam=0

for n in range(0,N):
    
    ad= random.randrange(d)
    secilenler.append(ad)
    odul= veriler.values[n,ad]
    toplam= toplam+odul
    
plt.hist(secilenler)
plt.show()
    
