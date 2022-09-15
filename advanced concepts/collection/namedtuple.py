from collections import namedtuple, Counter

Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc="Ford Engine", cost=1200.00, amount=10)
print(auto_parts.id_num)

Counter('superfluous')
counter = Counter('superfluous')
auto_parts = ('1234', 'Ford Engine', 1200.00, 10)
print(auto_parts[2])
id_num, desc, cost, amount = auto_parts
print(id_num)


# python dictionary to object
Parts = {'id_num': '1234', 'desc': 'Ford Engine', 'cost': 1200.00, 'amount': 10}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print('parts=', parts)

parts = namedtuple('Parts', Parts.keys())
print(parts)

auto_parts = parts(**Parts)
print('autoparts = ', auto_parts)