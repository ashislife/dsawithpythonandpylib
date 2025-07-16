import numpy as np
"""Arithmetic operator"""
# var=np.array([1,2,3,4,5])
# varadd=var+3
# print(varadd)
#
# var1=np.array([1,2,3,4,5])
# var2=np.array([2,3,4,5,6])
# varadd=var1+var2
# print(varadd)
#
#
#
# """2-d array"""
# var1=np.array([[1,2,3,4],[2,3,4,5]])
# var2=np.array([[1,2,3,4],[2,3,4,5]])
# varadd=var1+var2
# print(varadd)


"""Arithmetic functions"""
var=np.array([1,2,3,4,5,8,3,90])
print("Min value:",np.min(var),"Position:",np.argmin(var))
print("Max value:",np.max(var),"Position:",np.argmax(var))
print("Sorted value",np.sort(var))
print("Square root",np.sqrt(var))

print("sin value",np.sin(var))

print("Sorted value",np.cos(var))
print("comulitive sum value",np.cumsum(var))




