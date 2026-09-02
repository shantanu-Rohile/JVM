
# # empid= ['e101','e102','e103','e103','e105']

# # set1 = set(empid)
# # print(set1)

# set1 = {1,2,3,4,5,3,3,6,7}

# set1.update([99,88,100])

# print(set1) # set does not support indexing

# set1.remove(5)


# print(set1)

# set1.discard(999) # unlike remove when element is not in set it will not give any error


# print(set1.pop())
# set1.clear()
# print(set1)

# set1 = {1,2,3,4,5,3,3,6,7}

# print(1 in set1)


# print(1 not in set1)

# print(len(set1))

# set1 = {1,2,3,4,5,3,3,6,7,8,9}
# set2 = {24,43,44,55,54,65,9,8,88}

# res = set1 | set2
# print(res)

# res = set1.union(set2)
# print(sorted(res))


# set1 = {1,2,3,4,5,3,3,6,7,8,9}
# set2 = {24,43,44,55,54,65,9,8,88}

# res = set1 & set2

# print("Intersection : ",res)

# res = set1.intersection(set2)

# print("Intersection : ",res)

# res = set1 - set2

# print("diffrence : ",res)

# res = set1.difference(set2)

# print("diffrence : ",res)

# res = set1 ^ set2

# print("Symetric diffrence : ",res)

# res = set1.symmetric_difference(set2)

# print("Symetric diffrence : ",res)

# set1= {88,89}

# set2= {88,89,90,91,92}

# print("is subset : ",set1.issubset(set2))

# print("is superset : ",set2.issuperset(set1))

# set1= {888,989}

# set2= {88,89,90,91,92}

# print("is disjoint ? :", set1.isdisjoint(set2))


# set1= {1,2,3,45,55}

# list1 = list(set1)

# print(list1)

# print(type(list1))




## Case Study

# Imagine you work in an online shopping market, everyday we receive diffrenet customer id 


website_cust = {101,102,103,104,105}

mobile_cus = {103,104,105,106,107}

print("Customer using both mobile and website : ", (website_cust & mobile_cus))

print("All Unique customers : ", (website_cust | mobile_cus))

print("Customers using only mobile : ", (mobile_cus - website_cust))
