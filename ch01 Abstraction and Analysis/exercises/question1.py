#!/usr/bin/python3
"""
Create a list of one million integers numbered 0 to 999,999.
Time (using time.time function) the worst and best cases for
the list index method version of linear search, the linear search
code written using a for statement, and the binary search code.
In comments list the specifications of your computer (CPU chip and clock speed,
operating system and Python version) along with the worst and best times for
each of the three searches.
"""
from time import time


def linear_search1(items, target):
    """
    Searches for target in items.
    pre: items is an array with len(items) > 0, target is an integer.
    post: returns index (integer) of target if found, otherwise -1
    """

    if items.index(target):
        return items.index(target)
    else:
        return -1


def linear_search2(items, target):
    """
    Searches for target in items.
    pre: items is an array with len(items) > 0, target is an integer.
    post: returns index (integer) of target if found, otherwise -1
    """

    for i, item in enumerate(items):
        if items[i] == item:
            return i
    return -1


def binary_search(items, target):
    """
    Searches for target in items.
    pre: items is an array with len(items) > 0, target is an inteer.
    post: returns index (integer) of target if found, otherwise -1
    """

    low = 0
    high = len(items) - 1
    mid = (high + low) // 2

    while low < high:
        if target == mid:
            return mid
        elif target > mid:
            low = mid
            mid = (high + mid) // 2
        else:
            high = mid
            mid = (low + mid) // 2
    return -1


def function_timer(search1, search2, search3):
    """
    time execution of functions
    pre: search1, search2 and search3 are functions
    post: prints the best and worst times of received functions to STDOUT.
    """

    items = range(1000000)
    best_case_item = 10
    worst_case_item = 999999

    start = time()
    search1(items, best_case_item)
    stop = time()
    print('list.index() best case {}'.format(stop - start))

    start = time()
    search1(items, worst_case_item)
    stop = time()
    print('list.index() worst  case {}'.format(stop - start))

    start = time()
    search2(items, best_case_item)
    stop = time()
    print('list for-loop best case {}'.format(stop - start))

    start = time()
    search2(items, worst_case_item)
    stop = time()
    print('list for-loop worst case {}'.format(stop - start))

    start = time()
    search3(items, best_case_item)
    stop = time()
    print('binary search best case {}'.format(stop - start))

    start = time()
    search3(items, worst_case_item)
    stop = time()
    print('binary search worst case {}'.format(stop - start))


print('"list index()", "list for-loop()" &  "list binary search", starting...')

function_timer(linear_search1, linear_search2, binary_search)

# Intel Core i5 2.4ghz 64bit
# Linux Ubuntu
# Python 3.6.2
