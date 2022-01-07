def quicksort(seq, inicio, fim):
    '''Quick Sort'''

    if inicio < fim:
        divisor = particao(seq, inicio, fim)
        quicksort(seq, inicio, divisor)
        quicksort(seq, divisor+1, fim)


def particao(lista, esquerda, direita):
    pivot = lista[esquerda]
    p_esq = esquerda
    p_dir = direita
    while True:
        while lista[p_dir] > pivot:
            p_dir = p_dir - 1
        while lista[p_esq] < pivot:
            p_esq = p_esq + 1
        if p_esq < p_dir:
            lista[p_esq], lista[p_dir] = lista[p_dir], lista[p_esq]
            p_esq = p_esq + 1
            p_dir = p_dir - 1
        else:
            return p_dir
