m = map(ord, 'peter pan')

print(list(m))
# for temp in m:
#	print(temp)

ascii_values = [112, 101, 116, 101, 114, 32, 112, 97, 110]

"""
112

"""


def tag_it(av):
    return '<ascii char="{}">{}</ascii>'.format(chr(av), av)


m = map(tag_it, ascii_values)
m = map(lambda av: '<ascii char="{}">{}</ascii>'.format(chr(av), av), ascii_values)

for tag in m:
    print(tag)
