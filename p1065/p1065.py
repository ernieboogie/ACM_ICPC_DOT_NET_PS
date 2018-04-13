num = input("")

_sum = 0

for elem in range(num):
    elem = elem + 1

    if elem < 100:
        _sum = _sum + 1
    elif elem == 1000:
        pass
    else:
        _3 = elem / 100
        _2 = (elem - _3 * 100) / 10
        _1 = elem % 10

        if (_3 + _1) == _2 * 2 :
            _sum = _sum + 1


print _sum
