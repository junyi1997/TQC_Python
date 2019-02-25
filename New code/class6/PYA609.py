# -*- coding: utf-8 -*-
a=[]
b=[]
c=[]
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
for i in range(2):
    c.append([])
    for j in range(2):
        c[i].append(a[i][j]+b[i][j])
        print(c[i][j],end=" ")
    print()