def reverse_iterative(S):
    """Reverse elements in sequence S."""
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]  # swap first and last
        start, stop = start + 1, stop - 1  # narrow the range
