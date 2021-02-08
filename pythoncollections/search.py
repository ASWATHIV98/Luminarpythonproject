arr=[10,11,12,13,14]
element=int(input("enter elememt for search"))

flg=0
for num in arr:
    if(element==num):
        print(num)
        flg=1
        break
else:
    pass

