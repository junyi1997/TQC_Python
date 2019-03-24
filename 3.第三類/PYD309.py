# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:12:33 2018

@author: user

存款總額
"""

money=eval(input())
Amount=eval(input())
Month=int(input())
print('%s \t  %s' % ('Month', 'Amount'))
total=0.0
for i in range(1,Month+1):
    total=money+money*Amount/1200
    money=total
    print('%3d \t %.2f' % (i, total))