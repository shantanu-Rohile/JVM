# enter 3 number and find their sum and average?

num1 = int(input("Add first number : "))

num2 = int(input("Add Second number : "))

num3 = int(input("Add third number : "))

num = [num1,num2, num3]

print("Sum of numbers : ",sum(num))


print("Average of numbers : ",sum(num)/len(num))