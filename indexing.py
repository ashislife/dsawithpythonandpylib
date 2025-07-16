import numpy as np
"""1 dimension"""
var=np.array([45,7,9,5,1])
print(var)
print()
print(var[0])
print()
print("Dimension",var.ndim)



"""2 dimension"""
var1=np.array([[1,2,3],[4,5,6]])
print(var1)
print()
print(var1[1,2])
print()
print("Dimension",var1.ndim)
print(var1.shape)




"""3 dimension"""
var2=np.array([[[1,2],[2,3]]])
print(var2)
print("Shape:",var2.shape)
print("dimension:",var2.ndim)

