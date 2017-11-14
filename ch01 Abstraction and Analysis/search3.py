def search(items, target):
    """
    Searches for target in items
    pre: items in a non-empty array or any iterable
    post: returns the index of target in items if found, otherwise -1
    """
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1
