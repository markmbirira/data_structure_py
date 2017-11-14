def search(items, target):
    try:
        return items.index(target)
    except ValueError:
        return -1
