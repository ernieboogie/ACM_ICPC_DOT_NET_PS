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
numDict['9'] = 0

A = input()
B = input()
C = input()


for elem in str(A*B*C):
    numDict[elem] += 1

keys = numDict.keys()
keys.sort()

for key in keys:
    print numDict[key]
