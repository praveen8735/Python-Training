from time import sleep, ctime

while True:
    with open('testit', 'a') as fw:  # context manager 
        fw.write(ctime() + '\n')

    sleep(.5)