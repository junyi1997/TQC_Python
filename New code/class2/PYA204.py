# -*- coding: utf-8 -*-
#a=input()
#b=input()
#op=input()
#
#rea=a+op+b
#result=eval(rea)
#print(result)

a=eval(input())
b=eval(input())
op=input()
if op == "+":
    ans=a+b
elif op == "-":
    ans=a-b
elif op == "*":
    ans=a*b
elif op == "/":
    ans=a/b
elif op == "//":
    ans=a//b
elif op == "**":
    ans=a**b
print(ans)
