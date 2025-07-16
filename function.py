# tom_exp_list=[213,345,864,3]
# joe_exp_list=[21,345,864,3]
#
# total=0
# for i in tom_exp_list:
#     total=total+i
# print("Toms total",total)
#
#
# # last two code are same
# total=0
# for i in joe_exp_list:
#     total=total+i
# print("joes total",total)
#
# # total=0
# # for i in range(len(joe_exp_list)):
# #     total=total+joe_exp_list[i]
# # print("joes total",total)










# def calculate_total(exp):
#     total=0
#     for i in exp:
#         total=total+i
#     return total
#
# tom_exp_list=[213,345,864,3]
# joe_exp_list=[21,345,864,3]
#
# toms_total=calculate_total(tom_exp_list)
# joes_total=calculate_total(joe_exp_list)
#
# print("Toms total Expense:",toms_total)
# print("Joes total Expense:",joes_total)





# def sum(a,b):
#     total=a+b
#     return total
#
# n=sum(4,5)
# print("Total sum",n)




""" Local(inside the body decelered) VS global(outside the the body like eg total =0) variable """

# total=0
# def sum(a,b=0):
#     total=a+b
#     print("Print total inside the body:",total)
#     return total
# n=sum(5)
# print("Print total outside the body:",total)