def torres_hanoi(n, a, b, c):
    #Implementação das Torres de Hanói
    if n == 1: #Caso base
        print(f"Move o disco {n} de {a} para {c}")
    else: #Caso recursivo
        torres_hanoi(n-1, a, c, b)
        print(f"Move disco {n} de {a} para {c}")
        torres_hanoi(n-1, b, a, c)