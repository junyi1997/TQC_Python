# -*- coding: utf-8 -*-
dic={}
while True:
    print("key:",end="")
    key=input()
    if key == "end":
        break
    else:
        print("value:",end="")
        value=input()
        dic[key]=value

a=dic.keys()
b=dic.values()

for i in a:
    print("{:}: {}".format(i,dic[i]))
        




#key=[]
#value=[]
#while True:
#    print("key:",end="")
#    i=input()
#    if i == "end":
#        break
#    else:
#        print("value:",end="")
#        j=input()
#        if i in key:
#            key.append(i)
#            if j  in value:
#                value.append(j)
#key.sort()
#value.sort()
#for k in range(len(key)):
#    print("{:}: {:}".format(key[k],value[k]))
