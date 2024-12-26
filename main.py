# import os

# folders = os.mkdir("data")

# if(not os.path.exits("data")):
#     os.mkdir("data")

# for i in range(0, 100):
#     os.rename(f"data/Day{i + 1}")

# is checks for memory location
# == checks only values

a = (1, 2)
b = (1, 2)

print(a is b)
print(a == b)

c = 33
d = 33

print(c is d)
print(c == d)

