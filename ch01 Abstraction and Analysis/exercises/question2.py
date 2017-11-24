"""
Create a random list of 10,000, 100,000, and 1,000,000 integers with
each number between 1 and 10 million. Measure how long it takes to
sort each list using the built-in list's sort method. In comments, list
the specifications of your computer (CPU chip and took speed, operating
system and Python version) along with how long it took to sort each list.
Also include comments that indicate what you think the Theta classifiication
is for the sort method based on the running times.
"""

from time import time
import random

list1 = [random.randint(1, 10000000) for x in range(10000)]
list2 = [random.randint(1, 10000000) for x in range(100000)]
list3 = [random.randint(1, 10000000) for x in range(1000000)]

start = time()
list1.sort()
stop = time()
print('10,000 integers {}'.format(stop - start))


start = time()
list2.sort()
stop = time()
print('100,000 integers {}'.format(stop - start))

start = time()
list3.sort()
stop = time()
print('1,000,000 integers {}'.format(stop - start))

# Intel Core i5, 2.4ghz
# Python 3.6, Ubuntu 17.10

# 10,000 integers: 0.0028870105743408203

# 100,000 integers: 0.04234766960144043

# 1,000,000 integers: 0.6659455299377441

