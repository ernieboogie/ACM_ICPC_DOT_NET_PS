
_list = []
_input = input("")

for i in range(1000000):
    if i == 0:
        _list.append(0)
    elif i == 1:
        _list.append(1)
    elif i == 2:
        _list.append(1)
    else:
        if((i+1)%6 == 0):
            _list.append(min(_list[i-1]+1, _list[(i+1)/2-1]+1 , _list[(i+1)/3-1]+1))
        elif((i+1)%2 == 0):
            _list.append(min(_list[i-1]+1, _list[(i+1)/2-1]+1))
        elif((i+1)%3 == 0):
            _list.append(min(_list[i-1]+1, _list[(i+1)/3-1]+1))
        else:
            _list.append(_list[i-1]+1)

print _list[_input-1]
