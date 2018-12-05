def get_integers():
    """infinite stream"""
    i = 1

    while True:
        yield i
        i += 1


square = (item ** 2 for item in get_integers())


def take_n(count, seq):
    for element in range(count):
        yield next(seq)


for temp in take_n(5, square):
    print(temp)
