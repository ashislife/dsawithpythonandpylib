import numpy as np

"""shuffle function"""
# var=np.array([1,2,3,4,5])
# np.random.shuffle(var)
# print(var)

"""unique function"""
# var1=np.array([1,2,3,4,5,5,6,6,7,8,9,10])
# x=np.unique(var1,return_index=True,return_counts=True)
# print(x)



# """"Resize function"""
# var2=np.array([1,2,3,4,5,6])
# print("Dimension:",var2.ndim)
# y=np.resize(var2,(2,3))
# print(y)
# print("Dimension of output",y.ndim)
#
#
#
# var2=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print("Dimension:",var2.ndim)
# y=np.resize(var2,(3,3,3))
# print(y)
# print("Dimension of output",y.ndim)




var2=np.array([1,2,3,4,5,6])
print("Dimension:",var2.ndim)
y=np.resize(var2,(2,3))
print(y.flatten())
