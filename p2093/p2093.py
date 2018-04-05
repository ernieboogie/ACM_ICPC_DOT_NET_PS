
_list = []
for i in range(90):
    if i == 0:
        _list.append(1)
    elif i == 1:
        _list.append(1)
    elif i == 2:
        _list.append(2)
    else:
        _list.append(_list[i-1]+_list[i-2])

_input = input("")
print _list[_input-1]
