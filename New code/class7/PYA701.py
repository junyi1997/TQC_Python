# -*- coding: utf-8 -*-
num=[]
while True:
    num1=int(input())
    if num1 == -9999:
        break
    num.append(num1)
numn=tuple(num)
maxn=max(num)
minn=min(num)
sumn=sum(num)
print(numn)
print("Length:",len(num))
print("Max:",maxn)
print("Min:",minn)
print("Sum:",sumn)