def search(items, target):
    """
    Searches for target in items
    pre: items is an array or iterable, len(items) > 1
    post: returns the index (int) of target in items, else -1
    """
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
