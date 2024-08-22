def overlap(a, b):
    count = 0
    for item in a:
        for order in b:
            if item == order:
                count += 1
    return count