import numpy as np
# var=np.matrix([[1,2,3,4],[5,6,7,8]])
# print(var)
# print()
# """transpose matrix"""
# print(np.transpose(var))
# # print(var.T)


# """swapaxes """
# print()
# print(np.swapaxes(var,0,1))


# """inverse matrix"""
# var=np.matrix([[1,2],[3,4]])
# print(np.linalg.inv(var))



# """"power of matrix"""
# var=np.matrix([[1,2],[3,4]])
# print(var.dot(var))



# var=np.matrix([[1,2],[3,4]])
# print(var)
# print()
# """power calculate"""
# print(np.linalg.matrix_power(var,3))
#
# """calculate identity matrix"""
# print(np.linalg.matrix_power(var,0))
#
# """inverse*power"""
# print(np.linalg.matrix_power(var,-2))



"""determinant"""
var=np.matrix([[1,2],[3,4]])
print(np.linalg.det(var))
