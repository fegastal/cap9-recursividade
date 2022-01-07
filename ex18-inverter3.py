def inverte3(seq):
    if len(seq) == 1:
        return seq
    else:
        meio = len(seq) // 2
        return inverte3(seq[meio:]) + inverte3(seq[:meio])