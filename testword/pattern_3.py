n=int(input("enter num"))
limit=int(input("enter limit"))
lowlimit=int(input("enter the lower_limit"))
upplimit=int(input("enter the upper_limit"))
for i in range(1,(limit+1)):
    if i**n in range(lowlimit,upplimit):
         print(i**n)
