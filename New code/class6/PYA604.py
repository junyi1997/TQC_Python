# -*- coding: utf-8 -*-
#data=[34,18,22,32,18,29,30,38,42,18]
data=[]
maxcount=0
maxnum=0
for i in range(10):
    data.append(int(input()))

dataset=set(data)

for ev in dataset:
    num=data.count(ev)
    if num > maxcount:
        maxcount=num
        maxnum=ev
print(maxnum)
print(maxcount)
    