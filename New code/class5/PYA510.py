# -*- coding: utf-8 -*-
def compute():
    F=[0,1]
    num=int(input())
    for i in range(num-2):
        Fn=F[i]+F[i+1]
        F.append(Fn)
    
    for j in F:
        print(j,end=" ")
    print()
compute()