def factors(n):  # generator that computes factors
    for k in range(1, n + 1):
        if n % k == 0:  # divides evenly, thus k is a factor
            yield k  # yield this factor as next result
