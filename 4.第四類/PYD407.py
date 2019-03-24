# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:13:58 2018

@author: user

不定數迴圈-閏年判斷

"""

while True:
    year = int(input())
    if year == -9999:
        break
    else:
        if((year%4==0)and (year % 100 != 0 or year % 400 == 0)):
            print("{:} is a leap year.".format(year))
        else:
            print("{:} is not a leap year.".format(year))