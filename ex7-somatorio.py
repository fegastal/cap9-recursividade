def somat(n):
    if n == 0:
        return 0
    else:
        return n + somat(n-1)
