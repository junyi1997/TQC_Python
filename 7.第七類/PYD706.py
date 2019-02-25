# -*- coding: utf-8 -*-
d=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
c=[]
b=0
a=int(input())
for i in range(a):
    c=input()
    b=0
    for kkk in range(26):
        d[kkk]=0
    for k in range(len(c)):
        if(c[k]=="a" or c[k]=="A"):
            d[0]+=1  
        if(c[k]=="b" or c[k]=="B"):
            d[1]+=1  
        if(c[k]=="c" or c[k]=="C"):
            d[2]+=1  
        if(c[k]=="d" or c[k]=="D"):
            d[3]+=1  
        if(c[k]=="e" or c[k]=="E"):
            d[4]+=1  
        if(c[k]=="f" or c[k]=="F"):
            d[5]+=1  
        if(c[k]=="g" or c[k]=="G"):
            d[6]+=1  
        if(c[k]=="h" or c[k]=="H"):
            d[7]+=1  
        if(c[k]=="i" or c[k]=="I"):
            d[8]+=1  
        if(c[k]=="j" or c[k]=="J"):
            d[9]+=1  
        if(c[k]=="k" or c[k]=="K"):
            d[10]+=1 
        if(c[k]=="l" or c[k]=="L"):
            d[11]+=1  
        if(c[k]=="m" or c[k]=="M"):
            d[12]+=1  
        if(c[k]=="n" or c[k]=="N"):
            d[13]+=1  
        if(c[k]=="o" or c[k]=="O"):
            d[14]+=1  
        if(c[k]=="p" or c[k]=="P"):
            d[15]+=1  
        if(c[k]=="q" or c[k]=="Q"):
            d[16]+=1  
        if(c[k]=="r" or c[k]=="R"):
            d[17]+=1  
        if(c[k]=="s" or c[k]=="S"):
            d[18]+=1  
        if(c[k]=="t" or c[k]=="T"):
            d[19]+=1  
        if(c[k]=="u" or c[k]=="U"):
            d[20]+=1  
        if(c[k]=="v" or c[k]=="V"):
            d[21]+=1             
        if(c[k]=="w" or c[k]=="W"):
            d[22]+=1             
        if(c[k]=="x" or c[k]=="X"):
            d[23]+=1   
        if(c[k]=="y" or c[k]=="Y"):
            d[24]+=1             
        if(c[k]=="z" or c[k]=="Z"):
            d[25]+=1  
    for kk in range(26):
        if(d[kk]>0):
            b+=1;
    if(b==26):        
        print("True")
    else:
        print("False")
                      
            
      

        #for kk in range(26):    
        #     if(c[k].count(f[kk])>0 or c[k].count(f[kk+26])>0) :
        #         d[k]=1
#     for j in range(26):
#         if(d[j]==1):
#             e=1
#         else:    
#             e=0
#         d[j]=0
#     if(e==1):
#         print("True")
#     else:
#         print("False")


         
            
        
    

         
                 
          
     

