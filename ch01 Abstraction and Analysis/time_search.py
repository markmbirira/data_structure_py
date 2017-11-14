#!/usr/bin/python3

import time
from bsearch import search

items = range(1000000)  # create a big list

start = time.time()
search(items, 999999)  # look for the last item
stop = time.time()
print('last item {}'.format(stop - start))

start = time.time()
search(items, 499999)  # look for the middle item
stop = time.time()
print('middle item {}'.format(stop - start))

start = time.time()
search(items, 10)  # look for item near the front
stop = time.time()
print('item near the front {}'.format(stop - start))
