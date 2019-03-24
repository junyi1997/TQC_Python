# -*- coding: utf-8 -*-

#字串格式化輸出
a=input()
b=input()
c=input()
d=input()

print("|{:>10s} {:>10s}|".format(a,b))
print("|{:>10s} {:>10s}|".format(c,d))
print("|{:<10s} {:<10s}|".format(a,b))
print("|{:<10s} {:<10s}|".format(c,d))