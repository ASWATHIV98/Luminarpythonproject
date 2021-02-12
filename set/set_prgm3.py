lst=[1,2,3,4]
number=int(input("enter the number"))
st=set(lst)#{1,2,3,4}


# for num in st:
#     op=number-num#op=6-1=5,6-2=4
#     if op in st:#4 in st
#         print(num,op)   #2,4           #pair identifying
#         break
out=set()
for num in st:
    op=number-num
    if op in st:
        if op>num:
            out.add((num,op))
        else:
            out.add((op,num))
print(out)