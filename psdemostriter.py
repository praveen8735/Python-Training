s = 'this is a sample string'


for item in s:   # iterator
    if item not in 'aeiou ':    # membership test operator in, not in
        print(item, ':', ord(item))
    else:
        print('**')