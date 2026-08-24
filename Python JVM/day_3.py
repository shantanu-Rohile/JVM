
#relational operators

'''
a = 10
b = 20

print("a>b",a>b)
print("a==b",a==b)
print("a<b",a<b)
print("a!=b",a!=b)
print("a>=b",a>=b)
print("a<=b",a<=b)
print("a<b",a<b)
'''

#Logical operators

'''
a=10
b=20

print(not(a<=12 and b<=12))

print((a<=12 and b<=12))s

print((a<=12 or b<=12))
'''

# Test Case

'''

salary=30000

exp = 3

new_salary=30000 + 5000

print("salary > 25000", salary > 25000)

print("experience >= 2", exp >= 2)

print("salary > 25000 and new_salary > 25000 and exp >2", (salary > 25000) and (new_salary > 25000) and (exp >2))

'''

# Implicit Type Conversion


'''
a =10
b =10.2

res = a + b

print("Addition=", res)
'''

# Explicit Type Conversion
'''
a = "10"

print("The data type of a", type(a))

a=int(a)


print("value of a",a)

print("The data type of a", type(a))

'''

'''
# Type Conversion Test case

prev_name="raj"
name = str(prev_name)
age = "25"
salary="30000"

prev_name=str(prev_name)
age=int(age)
salary=float(salary)


print("name : ", type(prev_name))
print("age : ", type(age))
print("salary : ", type(salary))

prev_name1="mohit"
age1 = "30"
salary1 ="40000"

prev_name1=str(prev_name1)
age1=int(age1)
salary1=float(salary1)

print("name : ", type(prev_name1))
print("age : ", type(age1))
print("salary : ", type(salary1))


'''



a=10
b=a
print(id(a))
print(id(b))
