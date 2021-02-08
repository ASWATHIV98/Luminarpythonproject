 n=int(input("enter the limit"))
for i in range (0,n):
        for j in range(0, i+1):
            print("*",end="")
        print("")# it works at the time of j loop exit




# i=(0,3)
# j=(0,0+1)
# i=0
# j=(0,1)=*
# i=1
# j=(0,1)= *
         #  * *
#i=2
#j=(0,1,2)= *
          #  * *
           #  * * *