def impar(n):
    if n < 1:
        return False
    elif n == 1:
        return True
    elif par(n-1):
        return True
    else:
        return False