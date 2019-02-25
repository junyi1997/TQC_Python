# -*- coding: utf-8 -*-
#num=0.0
num=eval(input())
if num >= 38000:
    price=num*0.7
elif num >= 28000:
    price=num*0.8
elif num >= 18000:
    price=num*0.9
elif num >= 8000:
    price=num*0.95
print(price)    
