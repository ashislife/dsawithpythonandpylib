##create a empty class
# class A:
#     pass
#
# obj=A()



# ##create a class using bydefault constructor
# class A:
#     age=16
#     print(age)
# obj=A()



# ##create a class using create selfconstructor
# class A:
#     def __init__(selfself):
#         age = 16
#         print(age)
# obj=A()
# obj2=A()



#--------------------------------->

# class A:
#     "Learn Coding"
#     Age=10
#     print(Age)
#
# obj=A()
# print(A.Age)
# print(obj.Age)
# print(obj.__doc__)



#------------------------------------>
# class A:
#     age=10
#     def fun(self):
#         name="Ashish Kumar"
#         print(name)
#
# obj=A()
# obj.fun()
# print(obj.age)
# print(A.age)



#------------------------------>use function
# class A:
#     def  fun(self , age,name,Address):
#         print(age," ",age," ",Address)
#
# obj=A()
# obj.fun(10,"Ashish","MJH123")




#-------------------use constructor 
class A:
    def  __init__(self , age,name,Address):
        print(age," ",age," ",Address)

obj=A(10,"Ashish","MJH123")

