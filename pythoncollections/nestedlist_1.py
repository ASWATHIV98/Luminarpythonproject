employees=[
    [100,"tom","developer",25000],
    [101,"jack","qa",28000],
    [102,"rose","developer",25000],
    [103,"quin","se",30000]
]
sum=0
for employee in employees:
    print(employee[1])
for developer in employees:
    if(developer[2]=="developer"):
        print(developer)
for employee in employees:
    sum=sum+employee[3]
print(sum)

high=0
for employee in employees:
    if(employee[3]>high):
        high=employee[3]
print(high)