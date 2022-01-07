def anagrama(cad):
    if cad == '':
        return [cad]
    else:
        resp= []
        for perm in anagrama(cad[1:]):
            for pos in range(len(perm) +1):
                resp.append(perm[:pos] + cad[0] + perm[pos:])
        return resp