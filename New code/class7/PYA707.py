# -*- coding: utf-8 -*-
#x=["Math","Literature","English","History","Geography"]
#y=["Math","Literature","Chinese","Physical","Chemistry"]
x=[]
y=[]
print("Enter group X's subjects:")
while True:
    na=input()
    if na == "end":
        break
    x.append(na)
print("Enter group Y's subjects:")   
while True:
    na=input()
    if na == "end":
        break
    y.append(na)
xset=set(x)
yset=set(y)
a=list(xset | yset)#全部
b=list(xset & yset)#共同
c=list(yset - xset)#Y有X沒有
d=list((xset | yset)-(xset & yset))#都沒有
a.sort()
b.sort()
c.sort()
d.sort()
print(a)
print(b)
print(c)
print(d)

