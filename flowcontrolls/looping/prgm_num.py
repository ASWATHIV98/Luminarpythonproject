n=int(input("enter the num"))#3
pattern=""
total=0
for i in range(1,(n+1)):#1..3
   pattern=str(n)*i

   print(pattern)#3*1=3  3*2=33  3*333=33

   total+=int(pattern)

print(total)