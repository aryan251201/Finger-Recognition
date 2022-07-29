# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:10:27 2021

@author: user
"""

from keras.models import load_model
import cv2
import numpy as np

model = load_model('model.h5')

img = cv2.imread('test1.jpg')
img = cv2.resize(img,(32,32))
img = np.reshape(img,[1,32,32,3])

classes = model.predict_classes(img)

import RPi.GPIO as GPIO 
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True: # Run forever
    if classes==0:
        GPIO.input(10) == GPIO.HIGH  
        print("Button1 was pushed!== that's coke")

    if classes==1:
        GPIO.input(11) == GPIO.HIGH
        print("Button2 was pushed! == that's fanta")
    
    if classes==2:   
        GPIO.input(12) == GPIO.HIGH
        print("Button3 was pushed! == that's sprite")
        
    if classes==3:
        GPIO.input(13) == GPIO.HIGH
        print("Button4 was pushed! == that's mountain dew")
        
    if classes==4:
        GPIO.input(10) == GPIO.LOW
        GPIO.input(11) == GPIO.LOW
        GPIO.input(12) == GPIO.LOW
        GPIO.input(13) == GPIO.LOW
        print("Button5 was pushed! == so your glass if full")
