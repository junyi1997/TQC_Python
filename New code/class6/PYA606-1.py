# -*- coding: utf-8 -*-
def compute():  
    rclist=[]
    row=int(input())
    col=int(input())
    for r in range (row):
        rclist.append([])
        for c in range(col):
            rclist[r].append(c-r)
            print("{:4d}".format(rclist[r][c]),end="")
        print()
compute()
