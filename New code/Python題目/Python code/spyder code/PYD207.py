# -*- coding: utf-8 -*-

#1
total=0.0
a=eval(input())
if a >= 38000.0:
    total = a * 0.7
elif a >= 28000.0:
    total = a * 0.8
elif a >= 18000.0:
    total = a * 0.9
elif a >= 8000.0:
    total = a * 0.95
print(total)
input()