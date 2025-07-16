
import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

        #find the length
    def __len__(self):
        return self.n
    def append(self,item):
        if self.n==self.size:
            #resize
        self.__resize(self.size*2)

        #append
        self.A[self.n] = item
        self.n = self.n + 1







    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()

L = MeraList()
print(L)
print(len(L))




