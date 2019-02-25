# -*- coding: utf-8 -*-
#data=[89,78,67,80,75,98,77,89,76,60]
data=[]
for i in range(10):
    data.append(int(input()))
sum=0
maxnum=max(data)
minnum=min(data)
max1=data.remove(maxnum)
min1=data.remove(minnum)
for a in data:
    sum=sum+a
aver=sum/len(data)
print(sum)
print("{:.2f}".format(aver))