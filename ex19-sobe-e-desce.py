def sobe_e_desce(n):
    if n == 1:
        return [1, 1]
    else:
        return [n] + sobe_e_desce(n-1) + [n]