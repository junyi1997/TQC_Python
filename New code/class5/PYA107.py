# -*- coding: utf-8 -*-
a=[]
for i in range(1,6):
    a.append(eval(input()))

sum=0.0
for i in range(5):
    sum=sum+a[i]

aver=sum/len(a)
for i in a:
    print(i,end=" ")
print("")
print("Sum =",sum)
print("Average =",aver)

#a=[]
#for i in range(1,6):
#    a.append(eval(input()))
#
#sum=0
#for i in a:
#    sum=sum+i
#
#aver=sum/len(a)
#
#for i in a:
#    print(i,end=" ")
#print("")
#print("Sum = {:.1f}".format(sum))
#print("Average = {:.1f}".format(aver))