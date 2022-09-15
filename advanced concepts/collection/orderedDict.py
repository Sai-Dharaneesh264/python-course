from collections import OrderedDict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(d.items())
print('new_d:', new_d)

print('normal order')
print('------------')
for key in new_d:
    print(key, new_d[key])
print('reverse order')
print('------------')
for key in reversed(new_d):
    print(key, new_d[key])