# -*- coding: utf-8 -*-
a=[]
b=[]
c=[[],[]]
print("Enter matrix 1:")
for i in range (2):
    a.append([])
    for j in range(2):
        print("[{:}, {:}]: ".format(i+1,j+1),end="")
        a[i].append(int(input()))
print("Enter matrix 2:")
for i in range (2):
    b.append([])
    for j in range(2):
        print("[{:}, {:}]: ".format(i+1,j+1),end="")
        b[i].append(int(input()))
print("Matrix 1:")
for i in range(2):
    for j in range(2):
        print(a[i][j],end=" ")
    print()
print("Matrix 2:")
for i in range(2):
    for j in range(2):
        print(b[i][j],end=" ")
    print()
print("Sum of 2 matrices:")

c[0][0]=a[0][0]+b[0][0]
c[0][1]=a[0][1]+b[0][1]
c[1][0]=a[1][0]+b[1][0]
c[1][1]=a[1][1]+b[1][1]
for i in range(2):
    for j in range(2):
        print(c[i][j],end="")
    print("")
