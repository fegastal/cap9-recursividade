def figura(lado, angulo):
    '''Desenha figuras recursivamente a partir de um padrão base simples.
    Admite que a tartaruga tem a caneta levantada.'''

    pd()
    if lado:
        forward(lado)
        right(angulo)
        figura(lado-1, angulo)
    ht()
    return 0