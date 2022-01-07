def soma(m, n):
    if n == 0:
        return m
    else:
        return 1 + soma(m, n - 1)
