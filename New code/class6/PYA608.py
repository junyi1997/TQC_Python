# -*- coding: utf-8 -*-
#num=[[6,4,8],[39,12,3],[-3,49,33]]
num=[]
for i in range(3):
    num.append([])
    for j in range(3):
        num[i].append(int(input()))
print(num)
maxn1=num[0][0]
maxn2=num[0][0]
for a in range(3):
    for b in range(3):
        if maxn1 < num[a][b]:
            maxn1=num[a][b]
            a1=a
            b1=b
        elif maxn2 > num[a][b]:
            maxn2=num[a][b]
            a2=a
            b2=b
print("Index of the largest number {:} is: ({:}, {:})".format(maxn1,a1,b1))
print("Index of the smallest number {:} is: ({:}, {:})".format(maxn2,a2,b2))
