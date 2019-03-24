# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:19:41 2018

@author: user

詳細資料顯示

"""

fd=input()
d_li=0
d_w=0
d_ch=0
with open(fd,"r",encoding="utf-8") as fd:
    for data in fd:
        d_li+=1
        words=data.split()
        d_w=d_w+len(words)
        d_line="".join(words)
        d_ch=d_ch+len(d_line)
print("{:} line(s)".format(d_li))
print("{:} word(s)".format(d_w))
print("{:} character(s)".format(d_ch))