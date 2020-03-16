def fibo(limit):
    a, b = 0, 1
    fibo_list = []
    fibo_list.append(a)
    while len(fibo_list) < limit:
        a, b = b, a + b
        fibo_list.append(a)
    return fibo_list


def fibo_recursive(limit):
    if limit <= 1:
        return limit
    else:
        return fibo_recursive(limit - 1) + fibo_recursive(limit - 2)
