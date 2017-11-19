# Dataset.py
# TODO(Mark Mbirira): reimplement this using instance variables,
# self._size, self._min, self._max, self._sum and self._sum_squares which set
# The current implementation uses Theta(n)
# The new implementation uses Theta(1), has no loops


class Dataset(object):
    """Dataset is a collection of numbers from which simple
    descriptive statistics can be computed."""

    def __init__(self):
        """post: self is an empty Dataset"""

    def add(self):
        """add x to the data set
        post: x is added to the data set"""

    def min(self):
        """find the minimum
        pre: size of self >= 1
        post: returns smallest number in self"""

    def max(self):
        """find the maximum
        pre: size of self >= 1
        post: returns largerst number in self"""

    def average(self):
        """calculate the mean
        pre: size of self >= 1
        post: returns the mean of the value in self"""

    def std_deviation(nums):
        """calculate the standard deviation
        pre: size of self >= 2
        post: returns the standard deviation of the values in self"""

    def size(self):
        """size of self
        post: returns the size of self (number of values added)"""
