def demo(value):
    """generator function"""
    print('before 1')
    yield hex(value)
    print('after 1')

    print('before 2')
    yield bin(value)
    print('after 2')

    print('before 3')
    yield oct(value)
    print('after 3')


for item in demo(4):
    print(item)
    print('-' * 22)

"""print(demo())
g = demo()
print(next(g))
print('-' * 22)
print(next(g))
print('-' * 22)
print(next(g))
print('-' * 22)
print(next(g))
print('-' * 22)"""