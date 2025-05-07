# import math


# """floor value"""
# i = float(input("Enter the digit if you want to find the floor value: "))
# print("floor value",math.floor(i))







# """ceiling value"""
# i = float(input("Enter the digit if you want to find the ceiling value: "))
# print("ceiling value",math.ceil(i))






# """square root of float+integer """
# import math
# i = float(input("Enter the value if you want to find the square root: "))
# if i >= 0:
#     print("Square root:", math.sqrt(i))
# else:
#     print("Please enter a valid non-negative number.")
#
#
#
#
#
# """square root of integer """
# i = input("Enter a number to find its square root: ")
#
# if i.isdigit():
#     i = int(i)
#     print("Integer square root:", math.isqrt(i))
# else:
#     print("Please enter a valid non-negative integer.")




#
# var1=int(input("Enter the first value :"))
# var2=int(input("Enter the second value :"))
# print("Greatest Common Divisor (GCD) is :",math.gcd(var1,var2))
#



"""practical 1(b)"""
# import numpy as np
# var=np.array([23,45,76,12,90,32])
# print("Array is:",var)
# print()
# print("Dimensions are:",var.ndim)
# print()
# print("Shape:",var.shape)
# print("Sorted Array:",np.sort(var))
# print("Mean value :",np.mean(var))
# print("Total sum:",np.sum(var))
# print("sin value:",np.sin(var))


"""practical 1(c)"""
# import numpy as np
# var=np.matrix([[12,3],[6,45]])
# print(var)
# print(" Data Type is:",type(var))
# print("Dimension: ",var.ndim)
# print("Determinant of Matrix:",np.linalg.det(var))
# print("Eigen vector is:",np.linalg.eig(var))





# """practical 1(D)"""
# import numpy as np
# var=np.array([23,43,67,21,90,56])
# print(var)
# print("Dimensions:",var.ndim)
# print()
# x=var.reshape(3,2)
# print(x)
# print("Dimensions:",x.ndim)
# print()
# y=var.reshape(2,1,3)
# print(y)
# print("Dimension:",y.ndim)




# """practical 1(E)"""
# import numpy as np
# matrix=(np.random.randint(5,30,(3,3)))
# print(matrix)




# """practical 1(F)"""
# import numpy as np
# from scipy.linalg import det
#
# matrix = np.array([
#     [4, 2, 1],
#     [3, 0, 1],
#     [2, 1, 5]
# ])
# determinant = det(matrix)
# print("Matrix:")
# print(matrix)
# print("\nDeterminant of the matrix:", determinant)


# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
#
# plt.plot(x, y, label='sin(x)', color='blue', linestyle='--', marker='o')
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Line Plot Example")
# plt.legend()
# plt.grid(True)
# plt.show()



# import numpy as np
# from scipy.linalg import eig
#
# A = np.array([[4, -2],
#               [1,  1]])
#
# eigenvalues, eigenvectors = eig(A)
#
# print("Eigenvalues:\n", eigenvalues)
# print("\nEigenvectors:\n", eigenvectors)











#
#
# """peractical 1(G)"""
# import numpy as np
# var=np.matrix([[12,3],[6,45]])
# print(var)
# print(" Data Type is:",type(var))
# print("Dimension: ",var.ndim)
# print("Eigen value & Eigen vector Matrix:",np.linalg.eig(var))



#
# import pandas as pd
#
# """2(a)"""
# var=pd.Series(10,index=[1,2,3,4,5,6,7,8])
# print(var)
# print(type(var))
#
# print()
# """2(b)"""
# var=[21,32,54,66]
# print(pd.Series(var))
#
# print()
# """2(c)"""
# import numpy as np
# import pandas as pd
#
# print("Array using Numpy :",np.array([23,56,78,33]))
# print("Array using Pandas :",pd.Series([23,56,78,33]))
#
# print()
# """2(d)"""
# var=[21,32,54,66,32,867,]
# print(pd.Series(var,index=['a','b','c','d','e','f']))
#
# print()
# """2(E)"""
# var=[21,32,54,66,32,867,]
# print(pd.Series(var))
# print('Datatype',type(var))
# print()
# print(var[2])
#
#
# print()
# """2(F)"""
# dic={1:['a','b','c','d','e'],2:['f','g','h','i','j'],3:['k','l','m','n','o']}
# print(pd.DataFrame(dic))
#
#
#
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()





# """practical(3)"""
# print()

# import pandas as
