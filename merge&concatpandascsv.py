import pandas as pd


# var1=pd.DataFrame({"A":[1,2,3,4,5,6],"B":[11,21,23,44,56,52]})
# var2=pd.DataFrame({"A":[1,2,3,4,5,6],"C":[1,2,3,4,5,32]})
#
# """merge common attributes"""
# print(pd.merge(var1,var2,on="A"))
#
# print()
# """change the merge order"""
# print(pd.merge(var2,var1,on="A"))

# """--------><--------------------"""
# var1=pd.DataFrame({"A":[1,2,3,4,5,6],"B":[11,21,23,44,56,52]})
# var2=pd.DataFrame({"A":[1,2,3,4,5,7],"C":[1,2,3,4,5,32]})
# print(pd.merge(var1,var2,on="A"))
#
# print()
# """only return left and right is a missing data """
# print(pd.merge(var1,var2,how="left"))
# print()
# print(pd.merge(var1,var2,how="right"))

# print(pd.merge(var1,var2,how="outer",indicator=True))




# """------------------><-----------------------"""
# var1=pd.DataFrame({"A":[1,2,3,4,5,6],"B":[11,21,23,44,56,52]})
# var2=pd.DataFrame({"A":[1,2,3,4,5,6],"B":[11,21,23,44,56,52]})
# """show all the value if all attrubute databrame are same"""
# print(pd.merge(var1,var2,left_index=True,right_index=True))
#
# print()
#
# """change the schema name or attribute name"""
# print(pd.merge(var1,var2,left_index=True,right_index=True,suffixes=("name","id")))



# """------------>CONCATE<--------------------------"""
# """concate the series and create a new tableseries"""
# sr1=pd.Series([1,2,3,4])
# sr2=pd.Series([11,22,33,44])
# print(pd.concat([sr1,sr2]))
#
#
# print()
# """concate a dataframe """
# var1=pd.DataFrame({"A":[1,2,3,4,5,6],"B":[11,21,23,44,56,52]})
# var2=pd.DataFrame({"A":[1,2,3,4,5,7],"B":[111,211,213,414,516,521]})
# print(pd.concat([var1,var2]))
# print()
# print(pd.concat([var1,var2],axis=1))

print()
var1=pd.DataFrame({"A":[1,2,3,4,5,6],"B":[11,21,23,44,56,52]})
var2=pd.DataFrame({"A":[1,2,3,4,5,6],"C":[111,211,213,414,32,78]})

print()

print(pd.concat([var1,var2],axis=1,keys=["var1","var2"]))
print(pd.concat([var1,var2],axis=0,keys=["var1","var2"]))

