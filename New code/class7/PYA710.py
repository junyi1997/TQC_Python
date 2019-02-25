# -*- coding: utf-8 -*-
d={}
while True:
    print("Key:",end="")
    key=input()
    if key == "end":
        break
    else:
        print("Value:",end="")
        value=input()
        d[key]=value
print("Search key:",end="")
skey=input()
dk=d.keys()
if skey in dk:
    print("True")
else:
    print("False")
