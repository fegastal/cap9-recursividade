def figura_inc_lado_ang(lado, angulo, incl, inca):
    '''Desenha recursivamente com o incremento como parâmetro.'''
    pd()
    if lado > 0:
        forward(lado)
        right(angulo)
        figura_inc_lado_ang(lado-inc, angulo-inca, incl, inca)
    ht()
    return 0