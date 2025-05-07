import pandas as pd
# """Insert the new column """
# var=pd.DataFrame({'A':[1,2,3,4],'B':[9,4,6,3],'C':[6,1,7,4]})
# print(var)
# print()
# """copy the index C into a new column of Z"""
# var.insert(1,'Z',var['C'])
# print(var)


#
# """Insert the new column """
# var=pd.DataFrame({'A':[1,2,3,4],'B':[9,4,6,3],'C':[6,1,7,4]})
# print(var)
# print()
# """insert the new column in index Z"""
# var.insert(2,'Z',[5,2,7,3])
# print(var)
#
# print()
# """copy the limited data in insertion perpose using slicing"""
# var["Python_12"]=var["Z"][:2]
# print(var)











"""Delection"""
var=pd.DataFrame({'A':[1,2,3,4],'B':[9,4,6,3],'C':[6,1,7,4]})
var.pop('B')
print(var)
print()
"""Also use for delection"""
del var["A"]
print(var)