def prod(m, n):
    if n == 0:
        return 0
    else:
        return soma(m, prod(m, n - 1))
