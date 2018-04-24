
for test in range(input()):

    startEnd = map(int, raw_input("").split(" "))

    distance = startEnd[1] - startEnd[0]

    maxStep = 2
    result = 2
    if distance == 1:
        print 1

    elif distance == 2:
        print 2

    else:
        distance -= 2 # except first and last 1 step

        while distance > maxStep:
            if distance > 2 * maxStep:
                result += 2
                distance -= 2 * maxStep
            else:
                result += 1
                distance -= maxStep
            maxStep += 1

        result += 1

        print result
