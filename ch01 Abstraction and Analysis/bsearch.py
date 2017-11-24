"""
performs a binary search on an input of items.
"""


def search(items, target):
    """
    Searches for target in items
    pre: items is an iterable with len(items) > 0
    post: returns the index of an item if found, otherwise -1
    """
    low = 0
    high = len(items) - 1
    while low <= high:           # there is still a range to search
        mid = (low + high) // 2  # position of the middle item
        item = items[mid]
        if target == item:       # Found it, return the index
            return mid
        elif target < item:      # x is in lower half of range
            high = mid - 1       # move top marker down
        else:                    # x is in uppper half
            low = mid + 1        # move bottom marker up
    return -1
