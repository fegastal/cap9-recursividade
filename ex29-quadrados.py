def quadrado(lado):
    c = randint(0, 255)
    colormode(255)
    fillcolor(c, c, c)
    begin_fill()

    for i in range (4):
        fd(lado)
        rt(90)
    end_fill()