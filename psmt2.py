import threading
from time import sleep

n = 10


def worker():
    """child thread function"""
    t_name = threading.current_thread().name
    t_id = threading.current_thread().ident
    print('{} : {}'.format(t_name, t_id))
    sleep(n)


def main():
    """main thread function"""
    threads = list()

    for item in range(1, 6):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.setDaemon(True)
        t.start()

    print(threading.current_thread().name, 'prepares to terminate')


if __name__ == '__main__':
    main()
