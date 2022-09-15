from collections import deque 

import string 

d = deque(string.ascii_lowercase)
for letter in d:
    letter
d.append('bork')
print(d)
d.appendleft('test')
print(d)

d.rotate(1)
print(d)


def get_file(filename, n=5):

    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print('Error opening file: {}'.format(filename))
        raise
print(get_file('counter.py', 15))