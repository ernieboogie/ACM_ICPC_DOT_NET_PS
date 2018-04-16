def make_binary(_input):
    result = []

    while(_input >= 1):

        if _input % 2 == 0:
            result.append('0')
            _input = _input / 2
        else:
            result.append('1')
            _input = (_input - 1) / 2



    result.reverse()
    return result



_length = input("")
num = 0
for elem in make_binary(_length):

    if elem == '1':
        num = num + 1

print num
