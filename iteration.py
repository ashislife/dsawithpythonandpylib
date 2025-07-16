import numpy as np
var=np.array([9,8,7,6,5,4,3])
for i in var:
    print(i)




var1=np.array([[12,34,56],[65,43,22]])
print(var1)
print()
for i in var1:
    print(i)




"""2 dimension iteration """
var1=np.array([[12,34,56],[65,43,22]])
print(var1)
print()
for i in var1:
    for j in i:
        print(j)
"""iteration with the help of fuction"""
var1=np.array([[12,34,56],[65,43,22]])
print(var1)
print()
for i in np.nditer(var1):
    print(i)



