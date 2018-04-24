wordsDict = dict()
for ind in range(input()):

    words = raw_input("")
    if not len(words) in wordsDict:
        lengthList = []
        lengthList.append(words)
        wordsDict[len(words)] = lengthList
    else:
        lengthList = wordsDict[len(words)]

        if not words in lengthList:
            lengthList.append(words)
        wordsDict[len(words)] = lengthList


result = []
for ind in range(50):

    if ind in wordsDict:
        _list = wordsDict[ind]
        _list.sort()

        result += _list


for elem in result:

    print elem
