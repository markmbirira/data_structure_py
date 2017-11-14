"""
These loops execute sequentially, one right after the other.
So the total running time is O(n + n) which is still O(n),
because O(2n) has a constant which does not affect big O notation.
"""

n = input('enter n:')
for i in range(n):
    print i
for j in range(n):
    print j
