# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:56:28 2021

@author: Rishabh
"""

import pyautogui
from keras.models import load_model
import cv2
import numpy as np

model = load_model('modelg.h5')

#Fist - 0, Ok - 1, Swag - 2, Thumbs Down(D) - 3, Thumbs Up(U) - 4, Yo - 5

img = cv2.imread('test.jpg')
img = cv2.resize(img,(32,32))
img = np.reshape(img,[1,32,32,3])

classes = model.predict_classes(img)
print(classes)

if classes == 0:
    pyautogui.press("space")
if classes == 1:
    pyautogui.press("enter")
if classes == 2:
    pyautogui.hotkey('ctrl', 'Pgdn')   #open first document
if classes == 3:
    pyautogui.hotkey('ctrl', 'End')
if classes == 4:
    pyautogui.hotkey('ctrl', 'Home') 
if classes == 5:
    pyautogui.hotkey('ctrl','-') 
    

    
