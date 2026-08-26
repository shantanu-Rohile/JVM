# Update the first set with items that don’t exist in the second set


a = {1,2,3,4}

b = {3,4,5,6,7,8}


# a = a-b

a.difference_update(b)

print(a)