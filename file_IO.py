# open a file 
# f = open("myfile.txt")
# contents = f.read()
# f.close()

# print(contents)

# # write to a file
# f = open("myfile.txt", "a")
# f.write("Amazing")
# f.close()

# f = open("myfile.txt")
# contents = f.read()
# print(contents)

with open("myfile.txt", 'w') as f:
    f.write(" two")

