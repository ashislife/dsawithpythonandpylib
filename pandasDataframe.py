import pandas as pd

# list=[1,2,3,4,5,6,7]
# var=pd.DataFrame(list)
#
# print(var)
# print(type(var))


# """work with dictionary"""
# dic={'a':[1,2,3,4],'s':[8,4,7,3]}
# var=pd.DataFrame(dic)
# print(type(var))
# print(var)
#
#
# """work with specific column"""
# dic={'a':[1,2,3,4],'s':[8,4,7,3]}
# var=pd.DataFrame(dic,columns=['a'],index=['a','s','d','f'])
# print(type(var))
# print(var)



"""Display a specific colunms elements"""
# dic={'a':[1,2,3,4],'s':[8,4,7,3],'h':[32,5,8,2],5:[2,9,43,2]}
# var=pd.DataFrame(dic)
# print(type(var))
# print()
# print(var)
# print()
# print(var['h'][3])



"""work with list"""
list=[[1,2,3,4,5],[6,7,8,9,3],[1,5,3,7,8]]
var=pd.DataFrame(list)
print(type(var))
print(var)
