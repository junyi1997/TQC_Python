# -*- coding: utf-8 -*-
a=input()
b=len(a)
c=[0,0,0]
if(b>=8):
    c[0]+=1;
for i in range(b):
    if(a[i]>="A" and a[i]<="Z"):
        c[2]+=1
    if((a[i]>="A" and a[i]<="Z") or (a[i]>="a" and a[i]<="z") or (a[i]>="0" and a[i]<="9") ) :
        c[1]+=1
if(c[0]==1 and c[2]==1 and c[1]==b):        
    print("Valid password")   
else:
    print("Invalid password")     
        
