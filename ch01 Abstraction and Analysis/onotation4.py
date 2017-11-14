"""
The loop executes n times for each for each iteration of the first loop.
The print statement executes (n**2) times, thus has O(n2) running time.
Frequently, nested loops cause the running time to be the product of 
the number of times each loop executes.

"""

n = input('enter n: ')
for i in range(n):
    for j in range(n):
        print i, j
