# -*- coding: utf-8 -*-
a=int(input())
b=int(input())
c=[]
j=[]
sum=0
while a <= b:
    if (a % 4 == 0) or (a % 9 == 0):
        c.append(a)
        sum=sum+a
    a=a+1
for i in c:
    print("{:<4d}".format(i),end="")
    j.append(i)
    if len(j)==10:
        print("")
print("") 
print(len(c))   
print(sum)


#a=int(input())
#b=int(input())
#c=[]
#j=[]
#sum=0
#while a <= b:
#    if (a % 4 == 0) or (a % 9 == 0):
#        c.append(a)
#        sum=sum+a
#    a=a+1
#for i in c:
#    print("{:<4d}".format(i),end="")
#    j.append(i)
#    if len(j)==10:
#        print("")
#print("") 
#print(len(c))   
#print(sum)