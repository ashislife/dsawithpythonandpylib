d={"tom":1234,"joe":253,"soe":2986}
print(d)

"""add in dic"""
d["rob"]=768523
print(d)

"""delete any values"""
del d["joe"]
print(d)


"""retrieve values using iteration"""
for key in d:
    print("key:",key,"value:",d[key])


