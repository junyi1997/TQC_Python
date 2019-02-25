# -*- coding: utf-8 -*-
num1=[]
num2=[]
print("Create tuple1:")
while True:
    num=int(input())
    if num == -9999:
        break
    num1.append(num)
    
print("Create tuple2:")
while True:
    num=int(input())
    if num == -9999:
        break
    num2.append(num)
numtotal=num1[:]
numtotal.extend(num2)
numsort=numtotal[:]
numsort.sort()
print(numtotal)
print("Combined tuple before sorting:",tuple(numtotal))
print("Combined list after sorting:",numsort)