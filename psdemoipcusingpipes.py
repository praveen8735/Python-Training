import multiprocessing


def process_it(rd, wt):
    wt.send(rd.recv().upper())


def main():
    rd1, wt1 = multiprocessing.Pipe()
    rd2, wt2 = multiprocessing.Pipe()

    multiprocessing.Process(target=process_it, args=(rd1, wt2)).start()

    payload = 'a sample string'
    wt1.send(payload)
    response = rd2.recv()

    print('sent :', payload)
    print('recv :', response)


if __name__ == '__main__':
    main()
