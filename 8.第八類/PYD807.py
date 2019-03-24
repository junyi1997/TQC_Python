# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:18:34 2018

@author: user

字串加總

"""

val=input()
val=val.split(" ")
vl=list(map(eval,val))
print("Total = {:}".format(sum(vl)))
print("Average = {:}".format(sum(vl)/len(vl)))