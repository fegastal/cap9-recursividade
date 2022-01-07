def permuta(lst):
    if lst == []:
        return []
    else:
        resp = []
        for perm in permuta(lst[1:]):
            for pos in range(len(perm) + 1):
                resp.append(perm[:pos] + [lst[0]] + perm[pos:])
        return resp