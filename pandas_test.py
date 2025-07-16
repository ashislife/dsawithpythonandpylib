
# import pandas as pd

# df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
# std_dev_A = df['A'].std()
# std_dev_B = df['B'].std()

# print(std_dev_A)
# print(std_dev_B)



import pandas as pd
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)





import pandas as pd
data = [1, 2, 3, 4, 5]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print("Index:", series.index)
print("Values:", series.values)







import pandas as pd
data = [1, 2, 3, 4, 5]
print("value= ",data[2])










