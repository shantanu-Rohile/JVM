str="welcome to my blog"


print("1 : ",str[3:18])
print("2 : ",str[2:14:2])
print("3 : ",str[:7])
print("4 : " ,str[-9:-15]) # Here we are getting empty string because we have not added :-1 as step therefore python still takes +1 step
print("4 : " ,str[-9:-15:-1])
print("5 : " ,str[8:25:3])
print("6 : " ,str[0:9:3])

print(len(str))