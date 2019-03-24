# -*- coding: utf-8 -*-

#成績資料

with open("data.txt","a",encoding="utf-8") as fd:
    fd.write("\n")
    for i in range(5):
        fd.write(input())
        if i != 4:
            fd.write("\n")
with open("data.txt","r",encoding="utf-8") as fd:
    print("Append completed!")
    print("Content of \"data.txt\":")
    s=fd.read()
    print(s)