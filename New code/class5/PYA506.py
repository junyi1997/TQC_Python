# -*- coding: utf-8 -*-
#a=int(input())
#b=int(input())
#c=int(input())
#x1=0
#x2=0
#x1=(-1*b+(b**2-(4*a*c))**0.5)/2*a
#x1=(-1*b-(b**2-(4*a*c))**0.5)/2*a
#print(x1)
#print(x2)

def compute(a,b,c):
 
    x1=0
    x2=0
    if((b**2-4*a*c)<0):
        print("Your equation has no root.")
    else: 
        x1=((-1)*b+(b**2-4*a*c)**0.5)/(2*a)
        x2=((-1)*b-(b**2-4*a*c)**0.5)/(2*a)
        print("%.1f,"%x1,x2)  
        
a=int(input())  
b=int(input())
c=int(input()) 
compute(a,b,c)