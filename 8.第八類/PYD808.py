# -*- coding: utf-8 -*-
b=[0,0,0]
k=0
a=input()

for i in range(11):
    if(a[i]>='0' and a[i]<='9'):
        if(i<3):
            b[0]+=1
        elif(i<6):
            b[1]+=1
        else:
            b[2]+=1            
       
if(b[0]==3 and b[1]==2 and b[2]==4):
    print("Valid SSN")
else:
    print("Invalid SSN")
       
       

       
        

