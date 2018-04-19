import sys
from time import time

try:
    maxN = int(sys.argv[1])
except:
    maxN = 10000000
from time import time  # import time function from time module


def compute_average(n):
    """Perform n appends to an empty list and return average time elapsed."""
    data = []
    start = time()  # record the start time (in seconds)
    for k in range(n):
        data.append(None)
    end = time()  # record the end time (in seconds)
    return (end - start) / n  # compute average per operation


n = 10
while n <= maxN:
    print('Average of {0:.3f} for n {1}'.format(compute_average(n) * 1000000, n))
    n *= 10
