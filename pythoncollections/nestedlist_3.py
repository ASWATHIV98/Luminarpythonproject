employees=[
    [100,"tom","developer",25000,1989,1999],
    [101,"jack","developer",18000,1990,2005],
    [102,"jhon","ba",28000,1975,1988],
    [104,"dinu","qa",26000,1990,1999]
]
exp=[]
high=0
for employee in employees:
       exp.append(employee[5]-employee[4])
print("highest experience=",max(exp))
for employee in employees:
    if(employee[5]-employee[4]==max(exp)):
        print(employee)