# -*- coding: utf-8 -*-

#正n邊形面積計算

import math
c=eval(input())
a=int(input())

b=(c*a*a)/(4*math.tan(math.pi/c))
print("Area = {:.4f}".format(b))


