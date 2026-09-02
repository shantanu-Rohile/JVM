# student={
# "name":"jvm",
# "age":20}
# # print(student)
# student["city"]="Pune"
# student["age"]=22
# # print(student)
# # del student["age"]


# val = student.pop("age")

# # print(val)
# # print(student)


# # val = student.popitem()

# # print(val)
# # print(student)

# # student.clear()
# # print(student)

# # keys = list(student.keys())
# # values = list(student.keys())
# # items = list(student.items())
# # print("values : ",values)
# # print("keys : ",values)
# # print("item's : ",items)
# student={
# "name":"jvm",
# "age":20}
# student["city"]="Pune"
# student["age"]=22

# # print("city" in student)
# # print("Length : ", len(student))

# student = {
#     "name" : "shantanu rohile",
#     "detail":{
#         "age" : 22,
#         "city" : "Pune"
#     }
# }

# # print(student["detail"]["age"])
# # print("Length : ", len(student))

# # student={
# # "name":"jvm",
# # "age":30}

# # student.update({"age" : 22, "Course" : "Data Engineering"})

# # print(student)

# # How to update nested dictionary

# student = {
#     "name" : "shantanu rohile",
#     "detail":{
#         "age" : 22,
#         "city" : "Pune"
#     }
# }

# student["detail"].update({"age":23})
# student.update({"detail":{"age":33}})
# print(student)

# student2= student.copy()

# print(student2)

# student3 = dict(name = "JVM" , age = 5 )

# print(type(student3))

# print(student3)


# keys = [1,2,3]
# values = ["python", "sql", "Linux"]

# dic = dict(zip(keys,values))

# print(type(dict))
# print(dic)

# keys = ["python", "sql", "Linux"] 

# stud = dict.fromkeys(keys)

# print(sorted(stud))

student={
"name":"jvm",
"age":20,
"city" : "Pune"}

student.update({"caity" : "mumbai", "gpa" : 7.5})

del student["age"]

print(student)