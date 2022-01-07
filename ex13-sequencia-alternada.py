def alterna_plus(lst):
    if len(lst) == 1:
        return True
    elif lst[0] > lst[1]:
        return alterna_minus(lst[1:])
    else:
        return False

def alterna_minus(lst):
    if len(lst) == 1:
        return True
    elif lst[0] < lst[1]:
        return alterna_plus(lst[1:])
    else:
        return False

def alterna(lst):
    if len(lst) == 1:
        return True
    elif lst[0] > lst[1]:
        return alterna_minus(lst[1:])
    else:
        return alterna_plus(lst[1:])