# -*- coding: utf-8 -*-

#折扣方案

a=int(input())
if a>=8000:
    b=a*0.95  
elif a>=18000:
    b=a*0.9     
elif a>=28000:
    b=a*0.8      
elif a>=38000:
    b=a*0.7
print("{:.1f}".format(b))     

