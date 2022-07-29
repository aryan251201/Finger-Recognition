#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:20:50 2021

@author: chandresh
"""

from keras.models import load_model
import cv2
import numpy as np

model = load_model('model.h5')

img = cv2.imread('test.jpg')
img = cv2.resize(img,(32,32))
img = np.reshape(img,[1,32,32,3])

classes = model.predict_classes(img)

print(classes)


import I2C_LCD_driver
import time


mylcd = I2C_LCD_driver.lcd()


while True:
    mylcd.lcd_display_string(time.strftime('%I:%M:%S %p'), 1)
    mylcd.lcd_display_string(time.strftime('%a %b %d, 20%y'), 2)

import schedule
import subprocess
import time


def job(boo,c):
    while boo:
      subprocess.call(['mixkit-vintage-warning-alarm-990.wav'], shell=True)
      if(c == 4):
          break
      
b = True
schedule.every().day.at('7:00').do(job(b,classes))


while True:
    schedule.run_pending()
    time.sleep(1)    
    
