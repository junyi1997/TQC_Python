# -*- coding: utf-8 -*-
def compute(a,b):
    c=a.count(b)
    print("{:} occurs {:} time(s)".format(b,c))
    return c
a=input()
b=input()
compute(a,b)