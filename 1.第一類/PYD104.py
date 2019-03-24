# -*- coding: utf-8 -*-

#圓形面積計算
import math
r=eval(input())
Per=2*r*math.pi
a=r*r*math.pi
print("Radius = {:.2f}".format(r))
print("Perimeter = {:.2f}".format(Per))
print("Area = {:.2f}".format(a))