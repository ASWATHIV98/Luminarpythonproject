num1=int(input(" enter first num"))
num2=int(input("enter sec num"))
num3=int(input("enter third num"))




if(num1>num2)&(num1>num3):
    print(num1,"largest")
    if(num2>num3):
        print(num2,"second")
        print(num1,num2,num3)
    else:
        print(num3,"second")
        print(num1,num3,num2)
elif(num2>num3)&(num2>num1):
    print(num2,"largest")
    if(num3>num1):
        print(num3,"second")
        print(num2,num3,num1)
    else:
        print(num1,"second")
        print(num2,num1,num3)
elif(num3>num1)&(num3>num2):
    print(num3,"largest")
    if(num1>num2):
        print(num1,"second")
        print(num3,num1,num2)
    else:
        print(num2,"second")
        print(num3,num2,num1)

if(num1==num2)or(num1==num3)or(num2==num3):
    print("same number")

else:
    pass
