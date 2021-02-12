#update
#mutable
#using {}
#using key values{"jan":2000}
#key value must be unique
expens={"jan":20000,"feb":30000,"mar":40000,"aprl":50000,"may":60000}
print(expens["feb"])

expens["june"]=10000
print(expens)

if "july" in expens:
    print("exist")
else:
    expens["july"]=2000
    print(expens)