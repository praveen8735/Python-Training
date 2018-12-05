def argument_logger(func):
    """decorator"""

    def logger_handler(*args):
        value = func(*args)
        print('called {}{} return {} '.format(func.__name__, args, value))
        return value

    return logger_handler


class Math:
    def __init__(self, a, b):
        self.__compute(a, b)

    @argument_logger
    def __compute(self, a, b):
        return dict(result=a + b)


# compute = argument_logger(compute)
m = Math(12, 23)
m.__compute(12, 14)
