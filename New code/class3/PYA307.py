# -*- coding: utf-8 -*-
j=int(input())
for a in range(1,j+1):
    for b in range(1,j+1):
        print("{:<2d}* {:<2d}= {:<4d}".format(b,a,b*a),end="")
    print("")