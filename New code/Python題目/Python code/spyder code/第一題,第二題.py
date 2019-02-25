# -*- coding: utf-8 -*-
#吳驊涓／106111123
#第一題
"""
num=int(input("請輸入一個整數："))

if (num % 3 == 0) and (num % 5 == 0):
    print("%d 是三且五的倍數"%num)
elif num % 3 == 0:
    print("%d 是三的倍數"%num)
elif num % 5 == 0:
    print("%d 是五的倍數"%num)
else:
    print("%d 非三與五的倍數"%num)
input()
"""
num=int(input("請輸入一個整數："))
if (num % 3) == 0:
    if (num % 5) == 0:
        print("%d 是三且五的倍數"%num)
    else:
        print("%d 是三的倍數"%num)
else:
    if (num % 5) == 0:
        print("%d 是五的倍數"%num)
    else:
        print("%d 非三與五的倍數"%num)
input()
#---------------------------------------
#第二題
a=int(input("請輸入一個整數："))
b=int(input("請輸入一個大於a的整數："))
total=0
while a<=b:
    if a % 3 == 0:
        total = total+a
    a = a + 1
print("三倍數的總合為 %d" %(total))
input()