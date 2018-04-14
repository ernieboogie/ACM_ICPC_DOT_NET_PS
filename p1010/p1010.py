
def factorial(x):

    _sum = 1
    while(x > 0):
        _sum = _sum * x
        x = x - 1

    return _sum
def combination(x, y):

    return factorial(x) / (factorial(y) * factorial(x-y))



num_test = input("")

for test in range(num_test):

    test = []

    for elem in raw_input("").split(" "):
        test.append(int(elem))

    print combination(test[1], test[0])
