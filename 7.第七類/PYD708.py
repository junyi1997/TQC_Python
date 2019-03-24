
# -*- coding: utf-8 -*-
#詞典合併
a={}
b={}
print("Create dict1:")
while True:
    key = input("Key: ")
    if key == "end":
        break
    else:
        value = input("Value: ")
        a[key]=value
print("Create dict2:")
while True:
    key = input("Key: ")
    if key == "end":
        break
    else:
        value = input("Value: ")
        a[key]=value  
for i in b:
    a[i]=b[i]
c=list(a.keys())
cs=c.sort()
for i in c:
    print("{:}: {:}".format(i,a[i]))