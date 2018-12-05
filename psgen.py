"""
generators
    -expression
    -function

    all generators are iterators
"""

items = [item for item in range(1, 10)]
print(items)
print()

items = (item for item in range(1, 3))   # generator
print(items)
"""print()
print(next(items))
print(next(items))
print(next(items))"""

for i in items:
    print(i)