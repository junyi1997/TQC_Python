# -*- coding: utf-8 -*-

#浮點數格式化輸出
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())

print("|{:>7.2f} {:>7.2f}|".format(a,b))
print("|{:>7.2f} {:>7.2f}|".format(c,d))
print("|{:<7.2f} {:<7.2f}|".format(a,b))
print("|{:<7.2f} {:<7.2f}|".format(c,d))

