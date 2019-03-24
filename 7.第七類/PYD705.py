# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:17:12 2018

@author: user

子集合與超集合
"""

s1=set()
s2=set()
s3=set()
print("Input to set1:")
for i in range(5):
    n=int(input())
    s1.add(n)
print("Input to set2:")
for i in range(3):
    n=int(input())
    s2.add(n)
print("Input to set3:")
for i in range(9):
    n=int(input())
    s3.add(n)
print("set2 is subset of set1: {:}".format(s2.issubset(s1)))
print("set3 is superset of set1: {:}".format(s3.issuperset(s1)))