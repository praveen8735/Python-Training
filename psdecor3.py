from time import sleep, perf_counter


def timeit(func):
    def timeit_handler(*args):
        start_ts = perf_counter()
        value = func(*args)
        print('elapsed time :', perf_counter() - start_ts)
        return value

    return timeit_handler


@timeit
def demo():
    sleep(5)


demo()
print()
demo()
