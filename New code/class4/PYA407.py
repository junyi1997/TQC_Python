# -*- coding: utf-8 -*-
while True:
    year=int(input())
    if year==-9999:
        break
    elif (year%4==0)or (year%100!=0 and year%400==0):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
        
