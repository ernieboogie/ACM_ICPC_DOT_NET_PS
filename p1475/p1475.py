import math

numDict = dict()

numDict['0'] = 0
numDict['1'] = 0
numDict['2'] = 0
numDict['3'] = 0
numDict['4'] = 0
numDict['5'] = 0
numDict['6'] = 0
numDict['7'] = 0
numDict['8'] = 0

roomNumber = str(input())

for char in roomNumber:

    if char == '6' or char == '9':
        numDict['6'] += 1


    else:
        numDict[char] += 1

numDict['6'] = int(math.ceil(float(numDict['6']) / 2))

_max = 0
for key,val in numDict.items():
    if val > _max :
        _max = val

print _max
