import math

T_num = input("")


for test_case in range(T_num):
    test = raw_input("")
    test_set = []
    for elem in test.split(" "):
        test_set.append(float(elem))

    r1 = test_set[2]
    r2 = test_set[5]
    distance = (test_set[0] - test_set[3]) ** 2 + (test_set[1] - test_set[4]) ** 2
    distance = distance ** 0.5

    if r1 + r2 < distance:
        print 0
    elif r1 + r2 == distance:
        print 1
    else: # r1 + r2 > distance
        if abs(r1 - r2) == distance:
            if distance == 0:
                print -1
            else:
                print 1
        elif abs(r1 - r2) > distance:
            print 0
        else:
            print 2
