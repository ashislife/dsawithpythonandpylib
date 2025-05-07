list1=[]
print(type(list1))



list2=[10,'ashish',True,10.2,10]
print(type(list2))
print(list2)




#insert the item
list=[10,'ankit',True,10.7,10]
list.insert(2,'Ashish')
print(list)
print(list.index(10,1))



#copy method
list=[10,'ankit',True,10.7,10]
list1=list.copy()
print(list1)







#sorting

list=[24,5,2,4,5,32,889]
list.sort()
print(list)
#decending order
list.sort(reverse=True)
print(list)


#list comprehension
list=["Ashish","Ankit",'anita',"rohit ","rahul"]
a=[word for word in list if word.startswith("a")]
print(a)


#list unpacking
list=("Ashish","Rahul")
n1,n2=list
print(n1)
print(n2)
