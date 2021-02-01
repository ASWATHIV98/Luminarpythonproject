limit=int(input("enter the limit"))
i=1
ototal=0
etotal=0
while(i<=limit):
     if(i%2==0):
        etotal+=1
     else:
        ototal+=1
     i+=1
print(ototal)
print(etotal)