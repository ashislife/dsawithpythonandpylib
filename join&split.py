import numpy as np
# var=np.array([1,2,3,4])
# var1=np.array([2,3,4,5])
#
# ar=np.concatenate((var,var1))
# print(ar)
#
#
#
# """2 dim array"""
# var=np.array([[1,2],[3,4],[5,6]])
# var1=np.array([[2,4],[5,6],[8,9]])
#
# ar=np.concatenate((var,var1),axis=1)
# ar=np.concatenate((var,var1),axis=0)
# print(ar)



# """using stack"""
# var=np.array([1,2,3,4])
# var1=np.array([2,3,4,5])
#
# ar=np.vstack((var,var1))
#
# print(ar)

var=np.array([1,2,3,4,5,6])
print(var)
print()
ar=np.array_split(var,3)
print(ar)
print(type(ar))
print(ar[0])



