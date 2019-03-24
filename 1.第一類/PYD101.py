# -*- coding: utf-8 -*-
#整數格式化輸出

a=int(input())
b=int(input())
c=int(input())
d=int(input())

print("|{:>5d} {:>5d}|".format(a,b))
print("|{:>5d} {:>5d}|".format(c,d))
print("|{:<5d} {:<5d}|".format(a,b))
print("|{:<5d} {:<5d}|".format(c,d))