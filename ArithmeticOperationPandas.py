import pandas as pd

"""addition"""
var=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
print(var)
print()
var["C"]=var["A"]+var["B"]
print(var)


"""Substitution"""
var=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
print(var)
print()
var["C"]=var["A"]-var["B"]
print(var)

"""Multiplication"""
var=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
print(var)
print()
var["C"]=var["A"]*var["B"]
print(var)


"""division"""
var=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
print(var)
print()
var["C"]=var["A"]/var["B"]
print(var)

"""modulus"""
var=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
print(var)
print()
var["C"]=var["A"]%var["B"]
print(var)



"""logical operator"""
var=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
print(var)
print()
var["python"]=var["A"]>=3
'''Also apply for mor the one '''
var["python1"]=var["B"]>6
print(var)





