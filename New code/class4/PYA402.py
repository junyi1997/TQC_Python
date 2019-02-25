# -*- coding: utf-8 -*-
a=[]
while True:
    num=eval(input())
    if num == 9999:
        break
    a.append(num)
print(min(a))
