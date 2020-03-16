def fibo(limit):
    a, b = 0, 1
    fibo_list = []
    fibo_list.append(a)
    while len(fibo_list) < limit:
        a, b = b, a + b
        fibo_list.append(a)
    return fibo_list


def _fibo_recursive(limit):
    if limit <= 1:
        return limit
    else:
        return _fibo_recursive(limit - 1) + _fibo_recursive(limit - 2)


if __name__ == '__main__':
    print(fibo(9))
