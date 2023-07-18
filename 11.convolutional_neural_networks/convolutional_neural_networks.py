# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:07:05 2019

@author: suleyman.kaya
"""
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

esari = Sequential()

esari.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))
esari.add(MaxPooling2D(pool_size = (2, 2)))

esari.add(Convolution2D(32, 3, 3, activation = 'relu'))
esari.add(MaxPooling2D(pool_size = (2, 2)))
esari.add(Flatten())

esari.add(Dense(output_dim = 128, activation = 'relu'))
esari.add(Dense(output_dim = 1, activation = 'sigmoid'))

esari.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

training_set = train_datagen.flow_from_directory('veriler/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 1,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('veriler/test_set',
                                            target_size = (64, 64),
                                            batch_size = 1,
                                            class_mode = 'binary')

esari.fit_generator(training_set,
                         samples_per_epoch = 8000,
                         nb_epoch = 2,
                         validation_data = test_set,
                         nb_val_samples = 2000)


test_set.reset()
pred = esari.predict_generator(test_set,verbose=1)

pred[pred > .5] = 1
pred[pred <= .5] = 0

dosyaisimleri = test_set.filenames

test_labels = []

for i in range(203):
    test_labels.extend(np.array(test_set[i][1]))
    

sonuc = pd.DataFrame()
sonuc['dosyaisimleri']= dosyaisimleri
sonuc['tahminler'] = pred
sonuc['test'] = test_labels   

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(test_labels, pred)
print(cm)

