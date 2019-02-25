# -*- coding: utf-8 -*-
num=[]
while True:
    num1=input()
    num.append(num1)
    if (len(num)>5) and num1 == "end":
        break
num1=num.pop(-1)
print(tuple(num))
print(tuple(num[:3]))
print(tuple(num[len(num)-3:]))