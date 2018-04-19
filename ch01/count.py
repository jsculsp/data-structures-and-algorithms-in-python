def count(data, target):
    n = 0
    for item in data:
        if item == target:  # found a match
            n += 1
    return n
