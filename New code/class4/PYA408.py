# -*- coding: utf-8 -*-
a=[]
odd=0#奇數
even=0#偶數
for i in range(10):
    a.append(int(input()))
    if a[i] %2 ==0:
        even=even+1
    else:
        odd=odd+1

print("Even numbers:",even)
print("Odd numbers:",odd)