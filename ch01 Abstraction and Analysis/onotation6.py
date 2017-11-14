"""
Nested loop with the inner loop executing different number of times
during each iteration of the outer loop.

The outer loop executes n times and the inner loops executes
(n - 1) times each time till the end of the iteration.

Total number of iteration for the inner loop sum  1 + 2 + 3 + ... + n
Formula for finding the sum:
  (1 + 2 + 3 + ... + n)
+ (n + (n-1) + (n-2) + ... + 1)

Each column sums to n + 1 and they are n columns, rising this formula:
 n(n + 1) being as  double, n(n + 1)/2, expanding produces quaratic polynomial.
"""

n = input('enter n: ')
for i in range(n):
    for j in range(i, n):
        print i, j
