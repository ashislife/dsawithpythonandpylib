# #default constructor
# class A:
#     pass
# obj=A()


#
# #self constructor----------------------
# class A:
#     def __init__(self):
#         name="Ashish"
#         print(name)
# obj=A()
#
# #-------------->
# class B:
#     def __init__(self):
#         self.name="Ashish"
#         print(self.name)
#
# obj1=B()




# #default constructor---------------------------->
# class A:
#     name="Ashish"
#     Age=22
#     def __init__(self):
#         print(self.name)
#     def show(self):
#         print(self.Age)
# obj=A()
# obj.show()


# #parameterized constructor------------------------------>
# class B:
#     def __init__(self,Age,Name, Address):
#         print(Age," ",Name," ",Address)
#
# obj=B(22,"ashish","MJH123")


#-------------------------->
class A:
    name2="Mehra"
    def __init__(self,Age,Name ):

        print(Age,Name,self.name2)

obj1=A(18,"Ashish")
