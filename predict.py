#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 16:08:55 2021

@author: chandresh
"""

from keras.models import load_model
import cv2
import numpy as np

# model choice = model.h5 or modelg.h5

model = load_model('model.h5')

img = cv2.imread('test.jpg')
img = cv2.resize(img,(32,32))
img = np.reshape(img,[1,32,32,3])

classes = model.predict_classes(img)

print(classes)

#corresponding classes can be verified using the .docx file uploaded on Git