def search(items, target):
    """
    Searches for target in items
    pre: items is a non-empty array, target is a possible element in item
    post: returns the index of target in items if found, otherwise -1
    """
    i = 0
    while i < len(items):
        if items[i] == target:
            return i
        i += 1
    return -1
