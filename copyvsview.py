import numpy as np
var=np.array([1,2,3,4])
co=var.copy()
var[1]=40
print("var:",var)
print("copy:",co)

var=np.array([1,2,3,4])
vi=var.view()
var[1]=40
print("var:",var)
print("view:",vi)
