# -*- coding: utf-8 -*-
#money=int(input())
#Amount=eval(input())
#Month=int(input())
#a=[]
#b=[]
#for i in range(1,6):
#    a.append(i)
#print("{:5s}{:>11s}".format("Month","Amount"))
#for i in range(5):
#    money=money+money*Amount/1200
#    b.append(money)
#    print("{:^5d}{:12.2f}".format(a[i],b[i]))

m=int(input())
p=eval(input())
mon=int(input())
i=1
total=0
print("%s     %s"%("Month","Amount"))
while i < mon+1 :
  total=m+m*p/1200
  m=total
  print("%3d      %.2f"%(i,total))
  i=i+1
#money=int(input())
#Amount=eval(input())
#Month=int(input())
#a=[]
#b=[]
#for i in range(1,6):
#    a.append(i)
#print("{:<9s}{:>7s}".format("Month","Amount"))
#for i in range(5):
#    money=money+money*Amount/1200
#    b.append(money)
#    print("{:^5d}{:>12.2f}".format(a[i],b[i]))