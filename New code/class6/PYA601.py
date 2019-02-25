# -*- coding: utf-8 -*-
a=[]
sum=0
for i in range(12):
    a.append(int(input()))
k=0
for j in a:
    ind=a.index(j)
    if ind % 2 == 0:
        sum=sum+j
    k=k+1
    print("{:>3d}".format(j),end="")
    if k % 3 ==0:
        print("")
print(sum)

