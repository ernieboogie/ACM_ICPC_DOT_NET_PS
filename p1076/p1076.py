
value = dict()

value["black"] = [0,1]
value["brown"] = [1,10]
value["red"] = [2, 100]
value["orange"] = [3, 10 ** 3]
value["yellow"] = [4, 10 ** 4]
value["green"] = [5, 10 ** 5]
value["blue"] = [6, 10 ** 6]
value["violet"] = [7, 10 ** 7]
value["grey"] = [8, 10 ** 8]
value["white"] = [9,10 ** 9]

reg_val = 0
for i in range(3):
    _input = raw_input("")
    if i == 0:
        reg_val = reg_val + 10 * value[_input][0]
    elif i == 1:
        reg_val = reg_val + value[_input][0]
    else:
        reg_val = reg_val * value[_input][1]


print reg_val
