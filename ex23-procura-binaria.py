def procura_bin_rec(x, seq, inicio, fim):
    if inicio == fim:
        if seq[inicio] == x:
            return inicio
        else:
            return -1
    else:
        meio = (inicio + fim) / 2
        if x == seq[meio]:
            return meio
        elif x < seq[meio]:
            return procura_bin_rec(x, seq, inicio, meio-1)
        else:
            return procura_bin_rec(x, seq, meio+1, fim)