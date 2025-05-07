# import pandas as pd
# import math
#
# csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv")
# print(csv_1)

# """only get the index number """
# print(csv_1.index)
#


# print()
# """get the column name """
# print(csv_1.columns)
#
#
# """get min/max/50%,std,count ,mean ...."""
# print(csv_1.describe())
# print()
#
#
# print("\nVariance:\n", csv_1.var())
# print()
# median_values = csv_1.median()
# print("\nMedian of each numeric column:\n", median_values)

#
#
# """See the starting 5 data """
# print(csv_1.head())
# print(csv_1.head(2))
#
#
# print()
# """See the ending 5 data """
# print(csv_1.tail())
# print(csv_1.tail(2))
#
# print()
# """print fix ammount/range of data """
# print(csv_1[:2])
# print(csv_1[6:12])
# print(type(csv_1))
#
# print()
# """print index no as array """
# print(csv_1.index.array)
#
# print()
#
#
# """print index no as numpy array"""
# print(csv_1.to_numpy())
# print()
# """another way"""
# import numpy as np
# print(np.asarray(csv_1))
#
# """sort the index either ascending and decending order """
# print(csv_1.sort_index(axis=0,ascending=False))

#
# print()
# """change the particular data """
# csv_1.loc[1, "Name"] = "Python"
# # print(csv_1.loc[1])
# print(csv_1)
# print(csv_1.loc[[1, 3],['Name','Age']])
#
#
# print()
# '''use iloc function'''
# print(csv_1.iloc[2,1])
#
# print()
# """drop the column"""
# print(csv_1.drop("Age",axis=1))
#









import pandas as pd
import math

csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv")
print(csv_1)
print()

print(csv_1.describe())
print()

print("\nVariance:\n", csv_1.var())
print()
median_values = csv_1.median()
print("\nMedian of each numeric column:\n", median_values)



