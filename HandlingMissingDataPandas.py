import pandas as pd

var=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book10.csv")
print(var)
# print()
# """drop the missing value"""
# print(var.dropna())
# print()
# """drop along the column """
# print(var.dropna(axis=1))
# print(var.dropna(axis=0))

# print()
# """remove all nan values row """
# print(var.dropna(how="any"))

# print()
# """remove all nan values any particular column """
# print(var.dropna(subset=["Age"]))

# print()
# """remove all nan values your dataset"""
# print(var.dropna(inplace=True))



# print()
# """if any column only one nan value so drop this  """
# print(var.dropna(thresh=2))



# """fill the value in dataset """
# print()
# print(var.fillna("PYTHON"))
#
# """fill the particular data  in dataset """
# print()
# print(var.fillna({"Age":"PYTHON"}))

# """in the place of NaN value fill previous/backword data in your dataset """
# print()
# """forward value filled"""
# print(var.fillna(method="ffill"))
# """backword value filled"""
# print(var.fillna(method="bfill"))


# print()
# """fill value along the axis """
# '''along row'''
# print()
# print(var.fillna(method="bfill",axis=0))
# '''along column'''
# print(var.fillna(method="bfill",axis=1))


#
# """print same data inplace of NaN"""
#
# print(var.fillna(12,inplace=True))

print()
"""fill limited ammount of dataset """
'''first 2 data will filled'''
print(var.fillana("PyThOn",limit=2))