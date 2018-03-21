def mean(data):
    tot = 0
    count = 0

    for x in data:
        count += 1
        tot += x

    return tot / max(count, 1)
