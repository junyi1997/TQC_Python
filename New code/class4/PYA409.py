# -*- coding: utf-8 -*-
Nami=0
Chopper=0
scrap=0
for i in range(5):
    poll=int(input())
    if poll ==1:
        Nami=Nami+1
    elif poll ==2:
        Chopper=Chopper+1
    else:
        scrap=scrap+1
    print("Total votes of No.1: Nami = ",Nami)
    print("Total votes of No.2: Chopper = ",Chopper)
    print("Total null votes = ",scrap)
if Nami < Chopper:
    print("=> No.2 Chopper wins the election.")
elif Nami > Chopper:
    print("=> No.1 Nami wins the election.")
else:
    print("=> No one wins the election.")
