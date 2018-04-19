def factors(n):  # traditional function that computes factors
    results = []  # store factors in a new list
    for k in range(1, n + 1):
        if n % k == 0:  # divides evenly, thus k is a factor
            results.append(k)  # add k to the list of factors
    return results  # return the entire list
