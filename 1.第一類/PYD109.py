# -*- coding: utf-8 -*-

#正五邊形面積計算

import math
a=eval(input())
b=(5*a*a)/(4*math.tan(math.pi/5))
print("Area = {:.4f}".format(b))


