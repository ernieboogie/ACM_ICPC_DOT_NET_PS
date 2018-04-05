num_of_input = input("")
_list = []
for i in range(10):
    if i == 0:
        _list.append(1)
    elif i == 1:
        _list.append(2)
    elif i == 2:
        _list.append(4)
    else:
        _list.append(_list[i-1]+_list[i-2]+_list[i-3])

_inputs = []
for i in range(num_of_input):
    _input = input("")
    _inputs.append(_input)


for elem in _inputs:
    print(_list[elem-1])
