# -*- coding: utf-8 -*-

#社會安全碼

a=input()
al="1,2,3,4,5,6,7,8,9,0"
b=a.split("-")
x=0
y=0
if (len(b[0]) == 3) and (len(b[1]) == 2) and (len(b[2]) == 4):
   for i in range(len(a)):
       if a[i] in al:
           x+=1
       else:
            y+=1
if (x == 9) and (y==2):
    print("Valid SSN")
else:
    print("Invalid SSN")
       
       

       
        

