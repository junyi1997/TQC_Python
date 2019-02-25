# -*- coding: utf-8 -*-
def compute():  
    row=int(input())
    col=int(input())
    for r in range (row):
        for c in range(col):
            print("{:4d}".format(c-r),end="")
        print()
compute()