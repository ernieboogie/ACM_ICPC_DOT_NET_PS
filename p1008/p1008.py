_input = raw_input("")

num = []
for elem in _input.split(" "):
    num.append(float(elem))

print round(num[0] / num[1] , 30)
