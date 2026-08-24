# Total number of lines of text in file

with open("assets/test.txt","r") as file:
    data = file.read()
    lines = data.splitlines()
    print("Total number of lines in file:", len(lines))