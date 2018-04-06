

n = input("")
_sum = 0
_prev = 0
for i in range(n):

    if i == 0:
        _sum = 1
        _prev = 0
    elif i == 1:
        _sum = 2
        _prev = 1
    else:
        _temp = _sum
        _sum = _sum + _prev
        _prev = _temp



print _sum % 10007
