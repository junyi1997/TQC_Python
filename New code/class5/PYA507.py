# -*- coding: utf-8 -*-
def compute():
        num=int(input())
        if num == 1:
            print("Not Prime")
        elif num == 2:
            print("Prime")
        elif num < 0:
            print("Not Prime")
        elif (num-1)%2==0:
            print("Prime")
        else:
            print("Not Prime")
compute()







#    if (num % 2 !=0) and (num % 3 !=0) and (num % 5 !=0) and (num % 7 !=0) and (num % 9 !=0) and (num % 11 !=0) and (num % 13 !=0) and (num % 17 !=0) and (num % 19 !=0):
#        print("Prime")
#    else:
#        print("Not Prime")

