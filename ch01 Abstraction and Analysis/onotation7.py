"""
The value of n is halved (integer) until the last item is 1
The number of steps taken to reach 1 will be same as binary search.
The steps increase as the log (base 2) of the input n.
x = log2n, In many algorithms, the input is divided in half and we
end up with:
O(log2) is asyptotic notation
"""

n = input('enter n: ')
while n > 1:
    n = n // 2    # // is interger division
