from .base import *

DEBUG = True
# DEBUG = False

try:
    from .local import *
except ImportError:
    pass
