from functools import reduce

l = [1, 2, 3, 4, 3, 5, 6, 6, 7, 8, 9, 9]
print(l)

# using map
mapl = list(map(lambda x : x * x, l))
print(f"mapl : {mapl}")

# using filter
filterl = list(filter(lambda x : x > 58, mapl))
print(f"filterl : {filterl}")

# using Reduce
reducel = reduce(lambda x, y: x + y, filterl)
print(f"reducel : {reducel}")