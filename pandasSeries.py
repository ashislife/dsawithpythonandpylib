import pandas as pd

# x=[3,4,5,6,7]
# var=pd.Series(x)
# print(var)
# print(type(var))



#
# """change the index """
# x=[3,4,5,6]
# var=pd.Series(x,index=['a','s','h','i'])
# print(var)
# print(type(var))
#
# """change datatype"""
# x=[3,4,5,6]
# var=pd.Series(x,index=['a','s','h','i'],dtype="float",name="python")
# print(var)
# print(type(var))

"""Apply for dic"""
# dic={"name":['python','c','c++','java'],"por":[12,23,45,15],"rank":[1,2,4,3]}
# var1=pd.Series(dic)
# print(var1)


"""random series for 12 digits"""
# var=pd.Series(12,index=[1,2,3,4,5,6,7,8])
# print(var)
# print(type(var))



"""No broadcastion """
var=pd.Series(12,index=[1,2,3,4,5,6,7,8])
var1=pd.Series(12,index=[1,2,3,4])
print(var+var1)
print(type(var))
