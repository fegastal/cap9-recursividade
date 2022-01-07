def pir_rec(niveis):
    '''Desenha uma pirâmide.'''
    if niveis == 1:
        linha_rec()
    else:
        pir_rec(niveis-1)
        pu()
        setx(xcor() - ((niveis - 2) * lado - lado / 2)
        sety(ycor() - lado)
        pd()
        linha_rec(niveis)