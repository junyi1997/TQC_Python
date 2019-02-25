# -*- coding: utf-8 -*-
num=[]
while True:
    num1=int(input())
    if num1 == -9999:
        break
    num.append(num1)
numn=tuple(num)
print(numn)
print("Length:",len(num))
print("Max:",max(num))
print("Min:",min(num))
print("Sum:",sum(num))