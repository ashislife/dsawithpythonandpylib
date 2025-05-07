import pandas as pd
"""read the excel file"""

# csv_1=pd.read_excel("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book1.xlsx")
"""read the csv file"""

csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv")
print(csv_1)
print()
# """Find the particular row"""
# csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv",nrows=1)
# print(csv_1)
# print(type(csv_1))
# print()
# print()
# """find the particular column"""
# # csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv",usecols=['Name','Age'])
# """find with index"""
# csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv",usecols=[0,1])
# print(csv_1)
# print()
# print()
#
# """Skip the particular row"""
# csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv",skiprows=[1])
# print(csv_1)
# print()
# """change index with Age """
# csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv",index_col="Age")
# print(csv_1)
# print()
#
#
#
# """change header with his rows """
# csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv",header=2)
# print(csv_1)
#
# print()
# print()
# """create a new heading """
# # csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv",names=["NEW_HEADING"])
# csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv",names=["col1",'col2','col3','col4'])
# print(csv_1)
# print()
#
# """remove the header """
# # csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv",header=None,prefix="col")
# # print(csv_1)


# """change the datatype of any column """
# csv_1=pd.read_csv("C:\\Users\\ashis\\OneDrive\\Desktop\\python\\Book8.csv",dtype={"Salary":"float"})
# print(csv_1)
# print()
