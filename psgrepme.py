import re


pattern = 'bash$'

lines = filter(lambda line: re.search(pattern, line, re.I), open('/etc/passwd'))

for matched_line in lines:
    print(matched_line, end='')