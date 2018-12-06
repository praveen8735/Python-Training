"""demo for the bytes string"""

from subprocess import check_output
from sys import platform as P

if P in ['linux', 'darwin']:
    cmd = ['ls', '-l', '/etc/passwd']
else:
    cmd = ['ipconfig']

op = check_output(cmd)
print(op.decode('ascii'))
