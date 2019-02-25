## -*- coding: utf-8 -*-
#char=eval(input())
#if (char >="a" and char <="z") or (char >="A" and char <="Z"):
#    print(char,"is an alphabet.")
#elif type(char)==int:
#    print(char,"is a number.")
#else:
#    print("is a symbol.")

#
#str.isalpha() 所有字符都是字母
#str.isdigit() 所有字符都是数字
char=input()
if char.isalpha():
    print(char,"is an alphabet.")
elif char.isdigit():
    print(char,"is a number.")
else:
    print(char,"is a symbol.")