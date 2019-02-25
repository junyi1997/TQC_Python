# -*- coding: utf-8 -*-
a=int(input())
if a%3==0:
    if a%5==0:
        print(a,"is a multiple of 3 and 5.")
    else:
        print(a,"is a multiple of 3.")
elif a%5==0:
    print(a,"is a multiple of 5.")  
else:
    print(a,"is not a multiple of 3 or 5.")   

