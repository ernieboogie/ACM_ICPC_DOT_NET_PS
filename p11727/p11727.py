

input_num = input("")


_prev = 0
_sum = 0
for i in range(input_num):

    if i == 0:
        _sum = 1
        _prev = 0
    elif i == 1:
        _sum = 3
        _prev = 1
    else:
        _temp = _sum
        _sum = _sum + 2 * _prev
        _prev = _temp


print _sum % 10007
