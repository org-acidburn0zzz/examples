#!/usr/bin/env python2.6

# https://docs.python.org/3.10/whatsnew/2.6.html

from threading import Lock
from passed import passed

lock = Lock()
with lock:
    pass

passed()
