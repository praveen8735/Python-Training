def demo(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


demo('a', 'e', 1, 2, 3, lang='perl', reverse=True)
