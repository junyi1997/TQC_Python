# -*- coding: utf-8 -*-
import math
n=int(input())
s=int(input())
a=(n*s**2)/(4*math.tan(math.pi/n))
print("Area = {:.4f}".format(a))
