def par(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    elif impar(n-1):
        return True
    else:
        return False