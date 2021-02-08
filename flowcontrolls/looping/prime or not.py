#n=int(input("enter the num"))
#for i in range(2,n):#2...10

 #   if(n%i==0):#11%2=1
    #    print(" not prime")#not
    #else:
       # print("prime")#prime



n=int(input("enter n"))
flg=0
for i in range(2,n):
    if(n%i==0):
        flg=1
        break
    else:
        flg=0
if(flg==0):
    print("prime")
else:
    print("not prime")