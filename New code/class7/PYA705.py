# -*- coding: utf-8 -*-
#s1=[3,28,-2,7,39]
#s2=[2,77,0]
#s3=[3,28,12,99,39,7,-1,-2,65]
s1=[]
s2=[]
s3=[]
print("Input to set1:")
for i in range(5):
    s1.append(input())
print("Input to set2:")
for i in range(3):
    s2.append(input())
print("Input to set3:")
for i in range(9):
    s3.append(input())
set1=set(s1)
set2=set(s2)
set3=set(s3)
print("set2 is subset of set1: {:}".format(set2.issubset(set1)))
print("set3 is superset of set1: {:}".format(set3.issuperset(set1)))