import threading
from time import sleep
from random import random


def worker(delay):
    """child thread function"""
    t_name = threading.current_thread().name
    t_id = threading.current_thread().ident
    sleep(delay)
    print('{} waited for the : {}'.format(t_name, delay))


def main():
    """main thread function"""
    threads = list()

    for item in range(1, 6):
        rand_value = random()
        t = threading.Thread(target=worker, args=(rand_value,), name='t'+str(item))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(threading.current_thread().name, 'prepares to terminate')


if __name__ == '__main__':
    main()
