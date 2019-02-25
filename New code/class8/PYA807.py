# -*- coding: utf-8 -*-
a=input()
s=a.split(" ")
total=0
for i in s:
    total+=int(i)
aver=total/len(s)
print("Total = {:}".format(total))
print("Average = {:}".format(aver))