def procura_s(elem, seq):
    if len(seq) == 0:
        return False
    elif seq[0] == elem:
        return True
    else:
        return procura_s(elem, seq[1:])