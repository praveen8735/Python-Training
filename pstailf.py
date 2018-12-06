def tail_f(file_name):
    with open(file_name) as fp:  # context manager
        fp.seek(0, 2)

        while True:
            content = fp.read()
            if content:
                yield content


for lines in tail_f('testit'):
    print(lines)
