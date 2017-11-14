"""
This code sample has two nested loops, you might think it is O(n2),
but note the one loop always executes 10 times no matter the value of n.
By multiplying the their loop time, 10 * n, which is O(10n), O(n)
"""

n = input('enter n: ')
total = 0
for i in range(n):
    for j in range(10):
        print i, j
