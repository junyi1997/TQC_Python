# -*- coding: utf-8 -*-
num=[]
s=[]
a=[]
text=["1st","2nd","3rd"]
for i in range(3):
    num.append([])
    print("The {:s} student:".format(text[i]))
    for j in range(5):
        num[i].append(eval(input()))
for k in range(3):
    st=sum(num[k])
    aver=st/5
    s.append(st)
    a.append(aver)
    print("Student",k+1)
    print("#Sum {:}".format(s[k]))
    print("#Average {:.2f}".format(a[k]))
