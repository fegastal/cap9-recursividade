def capicua(seq):
    if (len(seq) == 0) or (len(seq) == 1):
        return True
    elif seq[0] == seq[-1]:
        return capicua(seq[1:-1])
    else:
        return False