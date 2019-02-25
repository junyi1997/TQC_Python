# -*- coding: utf-8 -*-
floor=int(input())
sum=0
for i in range(floor):
    num=int(input())
    copy=num
    sum=0    
    while num > 0:
        r=int(num%10)
        sum=sum+r
        num=(num-r)/10
    
    print("Sum of all digits of {:} is {:}".format(copy,sum))
#    if num ==13h:
        
            
        
