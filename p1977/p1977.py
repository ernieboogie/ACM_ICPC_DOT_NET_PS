import sys
_from = int(sys.stdin.readline().rstrip())
_to = int(sys.stdin.readline().rstrip())
_sum = 0
_min = 0
num_list = list(range(1, 101))
is_min = False
for _num in num_list:
    _num2 = _num * _num
    if _num2 >= _from and _num2 <= _to:
        _sum +=  _num2
        if not is_min:
            _min = _num2
            is_min = True


if _sum == 0:
    print(-1)
else:
    print(_sum)
    print(_min)
