from sys import getsizeof

items = list(range(1, 100000))

temp22 = [hex(i) for i in items]

m = map(hex, items)

print(getsizeof(m))
print(getsizeof(temp22))

for item in m:
    print(item)
