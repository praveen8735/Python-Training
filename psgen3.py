def demo(value):
    """co-routines"""
    for func in [hex, oct, bin]:
        yield func(value)


for item in demo(4):
    print(item)
