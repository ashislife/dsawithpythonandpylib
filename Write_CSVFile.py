import pandas as pd

dic={"A":[1,2,3,4,5,6],"B":[7,6,5,4,3,2],"C":[62,7,74,14,97,15],"C":[62,7,7,14,97,23]}
d=pd.DataFrame(dic)
print(d)
print()
d.to_csv("text_new2.csv",index=False,header=[132,564,895])







