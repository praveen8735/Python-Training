from random import shuffle

items = list(range(1, 200))
shuffle(items)
print(items)
print()

m = filter(lambda n: n % 7 == 0, items)
print(sorted(list(m)))
