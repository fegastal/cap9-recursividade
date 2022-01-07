def mdc(n, m):
    div_n = divisores(n)
    div_m = divisores(m)
    inter=intersect(div_n, div_m)
    return max(inter)

def divisores(num):
    return [i for i in range(1, num+1) if (num %i) == 0]

def intersect(11,12):
    return [i for i in ll if i in 12]
    