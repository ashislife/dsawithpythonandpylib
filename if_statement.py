# num=input("Enter a number: ")
# num=int(num)
# if num%2==0:
#     print("Number is EVEN ")
# else:
#     print("Number is ODD")


indian=["samosa","daal","naam"]
chinese=["Egg roll","pot stiker","Fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a dish name :")
if dish in indian:
    print("Indian")
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print("italian")
else:
    print("Nothing ")
