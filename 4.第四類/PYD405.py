# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:13:40 2018

@author: user

不定數迴圈-分數等級

"""

while True:
    num=int(input())
    if num == -9999:
        break
    elif num >=90:
        print("A")
    elif num >=80:
        print("B")
    elif num >=70:
        print("C")
    elif num >=60:
        print("D")
    elif num >=0:
        print("E")