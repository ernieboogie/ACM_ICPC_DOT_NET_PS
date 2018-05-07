import math

numList = []
numDict = dict()



for ind in range(input()):
    _input = input()
    numList.append(_input)

    if _input in numDict:
        numDict[_input] += 1
    else:
        numDict[_input] = 1

numList.sort()


# mean

print int(round(sum(numList) / float(len(numList))))

# median
if len(numList)  % 2 == 0:
    index1 = len(numList) / 2
    index2 = index1 + 1

    print "%0.1f" %(float(numList[index1 - 1] + numList[index2 - 1]) / 2)

else: #odd case
    index = int(math.floor(len(numList) / 2))
    print numList[index]

#mode
modeList = []
modeVal = 0

for key, val in numDict.items():

    if val > modeVal:
        modeVal = val

for key, val in numDict.items():

    if val == modeVal:
        modeList.append(key)

modeList.sort()
if len(modeList) == 1:
    print modeList[0]
else:
    print modeList[1]


# coverage
#find min , max

print max(numList) - min(numList)
