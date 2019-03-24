# -*- coding: utf-8 -*-

#公里英哩換算
a=eval(input())
b=eval(input())
c=eval(input())
hr=3600
km=hr/(a*60+b)*c
ft=km/1.6
print("Speed = {:.1f}".format(ft))

