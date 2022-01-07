def anag(cad):
    if cad == '':
        return [cad]
    else:
        return [perm[:pos] + cad[0] + perm[pos:] for perm in anag(cad[1:]) for pos in range(len(perm) +1)]