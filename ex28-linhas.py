def linha_rec(n):
    if n == 1:
        quadrado()
    else:
        linha_rec(n-1)
        pu()
        setx(xcor() + lado)
        pd()
        quadrado()