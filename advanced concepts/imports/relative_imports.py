"""
my_package/
    __init__.py
    subpackage1/
        __init__.py
        module_x.py
        module_y.py
    subpackage2/
        __init__.py
        module_z.py
    module_a.py
"""

from . import subpackage1
from . import subpackage2
from . import module_x
from . import module_y

from .module_y import spam as ham

