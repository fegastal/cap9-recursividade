def inter_all(11, 12):
    if 11 == []:
        return [12]
    elif 12 == []:
        return [11]
    else:
        aux_1 = [[11[0]] + temp for temp in inter_all(11[1:], 12)]
        aux_2 = [[12[0]] + temp for temp in inter_all(11, 12[1:])]
        return aux_1 + aux_2