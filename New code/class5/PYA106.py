# -*- coding: utf-8 -*-
x=eval(input())
y=eval(input())
z=eval(input())
sec=x*60+y
hr=3600
km=float(hr/sec*3)
ft=float(km/1.6)
print("Speed = {:.1f}".format(ft))