import pandas as pd

var=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book10.csv")
print(var)





print()

# """use replace function"""
# print(var.replace(to_replace=116393.0 ,value=654333))
# print(var.replace(to_replace="Person_1",value="Python"))

# """replace the serial no"""
# print(var.replace([1,2,3,4,5,6,7,8,9,10],100))




# """replace the alphabetical value"""
# print(var.replace("[A-Z a-z]","JAVA",regex=True))
# print(var.replace("[A-Z]","JAVA",regex=True))


#
# """replace the alphabetical value with the help of dectionary """
# print(var.replace({"Department":'[A-Z]'},22,regex=True))



# """replace forward/backword data over a place of 52.0"""
# print(var.replace(52.0,method='ffill'))
# print(var.replace(52.0,method='bfill'))

# """replace with range in forward/backword filling  """
# print(var.replace(52,method='ffill',limit=2))



# """interpolet"""
# print(var.interpolate())


# """fill the data linearly"""
# print(var.interpolate(method="linear"))

"""fill the data linearly with the help of axis parameter """

print(var.interpolate(method="linear",axis=0))

"""limit area"""
print(var.interpolate(limit_area="inside"))
print(var.interpolate(limit_area="outside"))





