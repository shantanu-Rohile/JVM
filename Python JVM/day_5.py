# age = [10,11,12,23]

# age[0] = 20

# print(age)

student = ["pratik",10.5,22,"raj",True]

# print(student[0])


# print(student[-2])

student[2] = "JVM"

# print(student[0:5:-1])

# print(student[0:5:2])

student = student[0:5:2]

# print("length of list: ",len(student))

student_2 = ["gojo", "satoru", "itadori"]

student = student + student_2

# print("length of list: ",len(student))

# print(student)ss

student.append("Pune")

# print(student)

student.insert(1,"Mumbai")

# print(student)


student.extend(["Tokyo", "Osaka", "Kyoto"])

student.remove("Mumbai")

# print(student)

student.pop(-1)

# print(student)

student.clear()

# print(student)

student = ["pratik",10.5,22,"raj",True]


del student[1:3]

# print("JVM" in student)

# print("JVM" not in student)

student = ["pratik",10.5,22,"raj",True]

# print(student.index(22))



marks = [100,66,88,43,39,35,35]
# print("main lsit",marks)
# new_marks_sort=sorted(marks)
# print("sorted list",new_marks_sort)
# marks_rev = marks.sort(reverse=True)
# print("reverse list : ",marks)

# marks = marks.reverse()

# print("reverse list : ",marks)

# new_list = marks.reverse()

# print("reverse list : ",new_list)



# marks = [100,66,88,43,39,35,35]

# nwelist = marks[::-1]

# print("reverse list : ",nwelist)

# print("main list : ",marks)

# marks.reverse()

# print(marks)



data=[
[10,20],
[40,50]
]
print(data[1][0])