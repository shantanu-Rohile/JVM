# Dict and List comprehension

list= [i*i for i in range (1,11) ]

print(list)

new_list= [i*i for i in range (1,11) if i % 2 == 0 ]

print(new_list)


new_dict = {i:i*i for i in range(1,11)}

print(new_dict)