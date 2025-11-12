# stdin_investigation.py

# read from the stdin stream

import sys

n = 1
for line in sys.stdin:
    print (f"{n}:{line}", end="")
    n += 1