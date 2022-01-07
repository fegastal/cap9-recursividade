def inter_all(11, 12, aux=[]):
    if 11 == []:
        return [aux + 12]
    if 12 == []:
        return [aux + 11]
        return inter_all(11[1:], 12, aux + [11[0]] + inter_all(11, 12 [1:], aux + [12[0]]))
    