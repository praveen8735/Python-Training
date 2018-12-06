from sys import stdout, stderr

def argument_logger(log_file='', file='stdout'):
    def callable_handler(func):
        """decorator"""

        def logger_handler(*args):
            value = func(*args)

            if file == 'stdout':
                print('called {}{} return {} '.format(func.__name__, args, value))
            elif file == 'stderr':
                print('called {}{} return {} '.format(func.__name__, args, value), file=stderr)
            else:
                with open(log_file, 'a') as fw:
                    print('called {}{} return {} '.format(func.__name__, args, value), file=fw)

            return value

        return logger_handler

    return callable_handler


@argument_logger()
def compute(a, b):
    return dict(result=a + b)


# compute = argument_logger('params.log)(compute)
print(compute(33, 44))
print()
print(compute(3.3, 4.4))
