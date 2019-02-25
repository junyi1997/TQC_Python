# -*- coding: utf-8 -*-
#num=int(input())
#if (num % 4 ==0) and not(num % 100 == 0):
#    if (num % 4 == 0) or (num % 400 == 0):
#        print(num,"is a leap year.")
#else:
#    print(num,"is not a leap year.")

#year=int(input())
#if year % 4 == 0:
#    if year % 400 ==0:
#        print(year,"is a leap year.")
#elif year % 400 ==0:
#    

year=int(input())
if (year % 400==0)or (year % 4 ==0 and year % 100 != 0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")