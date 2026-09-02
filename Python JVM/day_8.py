fz1 = frozenset([1,2,3])

# print(type(fz1))

# print(fz1)

fz2 = frozenset([2,3,3,4,5,6])


fz3 = frozenset([1,2,3,4])


# print(4 in fz3)

# print(44 not in fz3)


# res = fz2 | fz3
# res1 = fz2.union(fz3)

# print("Union : ",res)
# print("Union : ",res1)

# res = fz2 & fz3
# res1 = fz2.intersection(fz3)

# print("Intersection : ",res)
# print("Intersection : ",res1)

# res = fz2 - fz1
# res1 = fz2.difference(fz1)

# print("diffrence : ",res)
# print("diffrence : ",res1)


# res = fz2.symmetric_difference(fz1)
# print("symmetric diffrence : ",res)


# print(fz2.issubset(fz1))
# print(fz2.issuperset(fz1))
# print(fz2.isdisjoint(fz1))


# fz1 = frozenset([1,2,3,4])
# print(type(fz1))
# fz1 = frozenset((1,2,3,4))
# print(type(fz1))
# fz1 = frozenset({1,2,3,4})
# print(type(fz1))

# Test Case

# if we use lists

# emp1 = ["java","python","sql"]
# emp2 = ["java","sql","python"]

# if emp1==emp2 :
#      print("Lists : ","skills arew same") 
        
# else :
#      print("Lists : ","tehy have diffrent skill")  
   


# # if we use Tuple

# emp1 = ("java","python","sql")
# emp2 = ("java","sql","python")

# if emp1==emp2 :
#      print("Tuple : ","skills arew same") 
        
# else :
#      print("Tuple : ","tehy have diffrent skill")  
   


# # But if we use sets

# emp1 = {"java","python","sql"}
# emp2 = {"java","sql","python"}

# if emp1==emp2 :
#      print("Set : ","skills arew same") 
        
# else :
#      print("Lists : ","tehy have diffrent skill")  

# # But if we use frozenset

# emp1 = frozenset(["java","python","sql"])
# emp2 = frozenset({"java","sql","python"})

# if emp1==emp2 :
#      print("frozenset : ","skills arew same") 
        
# else :
#      print("frozenset : ","tehy have diffrent skill")  




#Dctionary


dic = {1:"apple", 2 : "banana", 3 : "cinemon" }

# print(dic.get(1))

# print(dic.keys())

# print(dic.values())

# print(dic.items())

# print(sorted(dic.items()))


# emp = {"id":101,"name":"shamtamu rohile","city":"pune","subjects":["python","sql","big data"]}

# print(type(emp))
# print(emp)


emp = {"id":101,"name":"shamtamu rohile","city":"pune","subjects":["python","sql","big data"]}

print(type(emp))
print(emp["id"])
print(emp["salary"])