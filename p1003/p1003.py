

num_case = input("")

for i in range(num_case):
    fib_list = []
    case_input = input("")

    for i in range(case_input+1):
        _fib = []

        if i == 0:
            _fib.append(1)
            _fib.append(0)
        elif i == 1:
            _fib.append(0)
            _fib.append(1)
        else:
            _fib.append(fib_list[i-1][0] + fib_list[i-2][0])
            _fib.append(fib_list[i-1][1] + fib_list[i-2][1])

        fib_list.append(_fib)

    print str(fib_list[case_input][0]) + " " + str(fib_list[case_input][1])
