# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:16:31 2018

@author: user

矩陣相加
"""

a=[]
b=[]
print("Enter matrix 1:")
for i in range(2):
    a.append([])
    for j in range(2):
        print("[%d, %d]: " % (i+1, j+1), end = '')
        a[i].append(int(input()))
        
print("Enter matrix 2:")
for i in range(2):
    b.append([])
    for j in range(2):
        print("[%d, %d]: " % (i+1, j+1), end = '')
        b[i].append(int(input()))

print("Matrix 1:")
for i in range(2):
    for j in range(2):
        print(a[i][j],end=" ")
    print("")
print("Matrix 2:")
for i in range(2):
    for j in range(2):
        print(b[i][j],end=" ")
    print("")

print("Sum of 2 matrices:")
a1=a[0][0]+b[0][0]
a2=a[0][1]+b[0][1]
a3=a[1][0]+b[1][0]
a4=a[1][1]+b[1][1]
print("{:} {:} ".format(a1,a2))
print("{:} {:} ".format(a3,a4))