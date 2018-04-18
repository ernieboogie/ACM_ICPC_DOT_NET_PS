def calc(planet, point):

    distance = (int(planet[0]) - point[0]) ** 2 + (int(planet[1])-point[1]) ** 2
    if (int(planet[2]) ** 2 > distance):
        return True
    return False
def isInPlanet(planet, start, dst):

    if calc(planet, start) and calc(planet,dst):
        return False
    elif calc(planet, start) or calc(planet, dst):
        return True
    else:
        return False

for test in range(input("")):
    numOfTry = 0
    start_point = raw_input("").split(" ")

    start = []
    dst = []
    start.append(int(start_point[0]))
    start.append(int(start_point[1]))
    dst.append(int(start_point[2]))
    dst.append(int(start_point[3]))

    for ind in range(input("")):
        info = raw_input("").split(" ")

        if isInPlanet(info, start, dst):
            numOfTry += 1

    print numOfTry
