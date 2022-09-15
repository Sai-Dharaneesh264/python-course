# try:
#     from http.client import responses
# except ImportError:
#     try:
#         from httplib import responses
#     except ImportError:
#         from BaseHTTPServer import BaseHTTPRequestHandler as _BHRH 
#     responses = dict([(k, v[0]) for k, v in _BHRH.responses.items()])


# try:
#     from urlparse import urljoin
#     from urllib2 import urlopen
# except ImportError:
#     from urllib.parse import urljoin
#     from urllib.request import urlopen


import sys

def square_root(a):
    import math
    return math.sqrt(a)

def my_pow(base_num, power):
    return math.pow(base_num, power)

if __name__ == '__main__':
    print(square_root(49))
    print(my_pow(2, 3))