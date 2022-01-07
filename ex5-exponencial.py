def exp(m, n):
    if n == 0:
        return 1
    else:
        return prod(m, exp(m, n - 1))
