import numpy as np
"""search"""
# var=np.array([1,2,3,4,5,56,2,8,26,8,1,9,2])
# x=np.where(var==2)
# print(x)


# var=np.array([1,2,3,4,5,6,8,9])
# x=np.searchsorted(var,7)
# print(x)

"""sort"""
# var=np.array([1,2,3,34,56,8,9])
# x=np.sort(var)
# print(x)
#
#
# var=np.array(["a","s","h","i","s","h"])
# x=np.sort(var)
# print(x)

"""filter """
var=np.array(["a","s","h","i","s","h"])
f=[True,True,True,False,False,False]
new_arr=var[f]
print(new_arr)


