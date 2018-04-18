def findRazer(_input):
    numOfRazer = 0
    prev = None
    for char in _input:
        if char == ')' and prev == '(':
            numOfRazer += 1

        prev = char

    return numOfRazer

def splitIron(_input):
    splitList = []
    splitCount = 0
    for point in range(len(_input)):
        if _input[point] == '(':
            splitCount += 1
        else:
            splitCount -= 1
        if splitCount == 0:
            if point != len(_input)-1:
                splitList.append(point)

    _inputList = list(_input)
    padding = 1
    for point in splitList:
        _inputList.insert(point + padding, '/')
        padding += 1
    return "".join(_inputList)

razer_info = raw_input("")
result = 0
ironInfo = splitIron(razer_info).split("/")

while(ironInfo != ['']):
    newIronInfo = []
    for iron in ironInfo:
        if iron[1:-1] != "":
            result = result + 1 + findRazer(iron[1:-1])
            newIronInfo.append(iron[1:-1])
    ironInfo = splitIron("".join(newIronInfo)).split("/")

print result
