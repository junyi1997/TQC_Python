# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:13:47 2018

@author: user

不定數迴圈-BMI計算

"""

while True:
    height=eval(input())
    if (height==-9999):
        break
    weight=eval(input())
    h=height/100
    BMI=weight/(h**2)
    print("BMI: {:.2f}".format(BMI))
    if BMI>=30:
        print("State: fat")
    elif BMI >=25:
        print("State: over weight")
    elif BMI >=18.5:
        print("State: normal")
    elif BMI <18.5:
        print("State: under weight")