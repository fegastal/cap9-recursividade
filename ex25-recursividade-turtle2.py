def figura_inc_lado(lado, angulo, inc):
    '''Desenha recursivamente com o incremento como parâmetro.'''
    pd()
    if lado > 0:
        forward(lado)
        right(angulo)
        figura_inc_lado(lado-inc, angulo, inc)
    ht()
    return 0