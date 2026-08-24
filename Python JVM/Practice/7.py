# Print random line from the code


import random


with open("assets/test.txt","r") as file:
    lines = file.readlines()
    random_line = random.choice(lines)
    print(random_line)