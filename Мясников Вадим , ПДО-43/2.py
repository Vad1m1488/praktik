c = [1, 4, 6]
d= [11, 33, 22]

res = [x for _, x in sorted(zip(d, c))]
print(res)