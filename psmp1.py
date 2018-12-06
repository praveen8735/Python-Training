import multiprocessing


def task_set():
    """child process function"""
    p_name = multiprocessing.current_process().name
    p_id = multiprocessing.current_process().pid

    print(p_name, ':', p_id)


def main():
    parent = multiprocessing.current_process()
    print(parent.name, '->', parent.pid)

    for item in range(1, 6):
        p = multiprocessing.Process(target=task_set)
        p.start()

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
