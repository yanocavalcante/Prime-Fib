def lin_fib(pos: int):
    if pos < 0:
        raise Exception
    elif pos <= 1:
        return pos
    aux1 = 1
    aux2 = 0
    for i in range(2, pos+1):
        res = aux1 + aux2
        aux2 = aux1
        aux1 = res
    return res

def rec_fib(pos: int):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return rec_fib(pos -1 ) + rec_fib(pos - 2)