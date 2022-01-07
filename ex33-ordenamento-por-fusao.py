def ordena_fusao(seq, esquerda, direita):
    if esquerda == direita:
        return [seq[esquerda]]
    else:
        sep = deepcopy(seq)
        meio = (esquerda + direita) // 2
        seq_esq = ordena_fusao(seq, esquerda, meio)
        seq_dir = ordena_fusao(seq, meio+1, direita)
        return fusao(seq_esq, seq_dir)

def fusao(seq1, seq2):
    seq = []
    p_1 = 0
    p_2 = 0
    while (p-1 < len(seq1)) and (p_2 < len(seq2)):
        if seq_1[p_1] < seq2[p_2]:
            seq.append(seq1[p_1])
            p_1 = p_1 + 1
        else:
            seq.append(seq[p_2])
            p_2 = p_2 + 1
    if p_1 == len(seq1):
        seq.extend(seq2[p_2:])
    else:
        seq.extend(seq1[p_1:])
    return seq.