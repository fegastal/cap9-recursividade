def inverte2(seq):
    if len(seq) == 0:
        return seq
    else:
        return seq[-1] + inverte2(seq[:-1])