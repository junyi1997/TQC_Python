# -*- coding: utf-8 -*-
f_name=input()
rd=open(f_name,"r",encoding="UTF-8")
n_line=0
n_word=0
n_ch=0
for eachline in rd:
    n_line+=1
    words=eachline.strip("\n").split(" ")
    n_word=n_word+len(words)
    newline="".join(words)
    n_ch=n_ch+len(newline)
rd.close()

print("{:} line(s)".format(n_line))
print("{:} word(s)".format(n_word))
print("{:} character(s)".format(n_ch))
