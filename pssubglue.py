"""process manager"""
import subprocess

cat = subprocess.Popen(['cat', '/etc/passwd'], stdout=subprocess.PIPE)

tr = subprocess.Popen(['tr', 'a-z', 'A-Z'], stdin=cat.stdout, stdout=subprocess.PIPE)

nl = subprocess.Popen(['python', 'psnl.py'], stdin=tr.stdout, stdout=subprocess.PIPE)


for line in nl.communicate():
    if line:
        print(line.decode('ascii'))


# commands